import React, { useEffect, useRef, useState } from 'react';
import usePrefersReducedMotion from '../../hooks/usePrefersReducedMotion';
import styles from './InteractiveBackground.module.css';

export function InteractiveBackground() {
  const canvasRef = useRef(null);
  const wrapperRef = useRef(null);
  const prefersReducedMotion = usePrefersReducedMotion();

  const [mousePos, setMousePos] = useState({ x: 0, y: 0 });
  const [targetMousePos, setTargetMousePos] = useState({ x: 0, y: 0 });
  const [spotlightActive, setSpotlightActive] = useState(false);

  // Spotlight and parallax loop values
  const currentPos = useRef({ x: 0, y: 0 });

  useEffect(() => {
    const handleMouseMove = (e) => {
      // Relative values [-1, 1] for parallax
      const rx = (e.clientX / window.innerWidth - 0.5) * 2;
      const ry = (e.clientY / window.innerHeight - 0.5) * 2;
      setTargetMousePos({ x: rx, y: ry });

      // Absolute pixels for spotlight CSS variables
      if (wrapperRef.current) {
        wrapperRef.current.style.setProperty('--sx', `${e.clientX}px`);
        wrapperRef.current.style.setProperty('--sy', `${e.clientY}px`);
      }
    };

    const handleMouseEnter = () => setSpotlightActive(true);
    const handleMouseLeave = () => setSpotlightActive(false);

    window.addEventListener('mousemove', handleMouseMove, { passive: true });
    document.body.addEventListener('mouseenter', handleMouseEnter);
    document.body.addEventListener('mouseleave', handleMouseLeave);

    return () => {
      window.removeEventListener('mousemove', handleMouseMove);
      document.body.removeEventListener('mouseenter', handleMouseEnter);
      document.body.removeEventListener('mouseleave', handleMouseLeave);
    };
  }, []);

  // Parallax animation frame loop
  useEffect(() => {
    if (prefersReducedMotion) return;

    let frameId;
    const LERP = 0.05;

    const animate = () => {
      currentPos.current.x += (targetMousePos.x - currentPos.current.x) * LERP;
      currentPos.current.y += (targetMousePos.y - currentPos.current.y) * LERP;

      if (wrapperRef.current) {
        wrapperRef.current.style.setProperty('--mx', currentPos.current.x.toFixed(4));
        wrapperRef.current.style.setProperty('--my', currentPos.current.y.toFixed(4));
      }
      frameId = requestAnimationFrame(animate);
    };

    frameId = requestAnimationFrame(animate);
    return () => cancelAnimationFrame(frameId);
  }, [targetMousePos, prefersReducedMotion]);

  // Particle System Effect (using Canvas)
  useEffect(() => {
    const canvas = canvasRef.current;
    if (!canvas) return;
    const ctx = canvas.getContext('2d');
    if (!ctx) return;

    let w = (canvas.width = window.innerWidth);
    let h = (canvas.height = window.innerHeight);

    const handleResize = () => {
      w = canvas.width = window.innerWidth;
      h = canvas.height = window.innerHeight;
    };
    window.addEventListener('resize', handleResize);

    const isMobile = window.innerWidth < 768;
    const count = isMobile ? 30 : 75;

    class Particle {
      constructor(init = false) {
        this.reset(init);
      }

      reset(init = false) {
        this.x = Math.random() * w;
        this.y = init ? Math.random() * h : h + 10;
        this.r = Math.random() * 2 + 0.3;
        this.vx = (Math.random() - 0.5) * 0.3;
        this.vy = -(Math.random() * 0.5 + 0.15);
        this.a = 0;
        this.maxA = Math.random() * 0.5 + 0.1;
        this.speed = Math.random() * 0.005 + 0.002;
        this.fading = false;

        const palettes = [
          ['rgba(124, 58, 237, ', 'rgba(79, 70, 229, ', 'rgba(167, 139, 250, '],
          ['rgba(37, 99, 235, ', 'rgba(96, 165, 250, ', 'rgba(34, 211, 238, '],
          ['rgba(255, 255, 255, ']
        ];
        const p = palettes[Math.floor(Math.random() * palettes.length)];
        this.colorStr = p[Math.floor(Math.random() * p.length)];
        this.glowRadius = this.r * (Math.random() * 5 + 4);
      }

      update() {
        this.x += this.vx;
        this.y += this.vy;

        if (!this.fading && this.a < this.maxA) {
          this.a += this.speed;
        }
        if (this.y < h * 0.1) {
          this.fading = true;
        }
        if (this.fading) {
          this.a -= this.speed * 1.6;
        }
        if (this.a <= 0 && this.fading) {
          this.reset(false);
        }
      }

      draw() {
        // Glowing aura
        const g = ctx.createRadialGradient(this.x, this.y, 0, this.x, this.y, this.glowRadius);
        g.addColorStop(0, this.colorStr + (this.a * 0.85).toFixed(3) + ')');
        g.addColorStop(1, this.colorStr + '0)');

        ctx.beginPath();
        ctx.arc(this.x, this.y, this.glowRadius, 0, Math.PI * 2);
        ctx.fillStyle = g;
        ctx.fill();

        // Core particle
        ctx.beginPath();
        ctx.arc(this.x, this.y, this.r, 0, Math.PI * 2);
        ctx.fillStyle = this.colorStr + Math.min(this.a * 2, 1).toFixed(3) + ')';
        ctx.fill();
      }
    }

    const particles = Array.from({ length: count }, (_, i) => new Particle(i < count));

    let animId;
    const tick = () => {
      ctx.clearRect(0, 0, w, h);
      if (!prefersReducedMotion) {
        particles.forEach((p) => {
          p.update();
          p.draw();
        });
      }
      animId = requestAnimationFrame(tick);
    };

    tick();

    return () => {
      window.removeEventListener('resize', handleResize);
      cancelAnimationFrame(animId);
    };
  }, [prefersReducedMotion]);

  // Aurora blobs slow hover animations
  const auroraParallaxStyle = (depth) => {
    if (prefersReducedMotion) return {};
    const dx = currentPos.current.x * depth * window.innerWidth;
    const dy = currentPos.current.y * depth * window.innerHeight;
    return {
      transform: `translate3d(${dx.toFixed(1)}px, ${dy.toFixed(1)}px, 0)`
    };
  };

  return (
    <div ref={wrapperRef} className={styles.wrapper} aria-hidden="true">
      <canvas ref={canvasRef} className={styles.canvas} />
      
      <div className={styles.aurora}>
        <div className={`${styles.blob} ${styles.blob1}`} style={auroraParallaxStyle(0.018)} />
        <div className={`${styles.blob} ${styles.blob2}`} style={auroraParallaxStyle(0.028)} />
        <div className={`${styles.blob} ${styles.blob3}`} style={auroraParallaxStyle(0.012)} />
        <div className={`${styles.blob} ${styles.blob4}`} style={auroraParallaxStyle(0.022)} />
      </div>

      <div 
        className={styles.grid} 
        style={prefersReducedMotion ? {} : {
          transform: `translate3d(calc(var(--mx, 0) * -6px), calc(var(--my, 0) * -6px), 0)`
        }} 
      />

      <div className={`${styles.spotlight} ${spotlightActive ? styles.spotlightActive : ''}`} />
    </div>
  );
}
export default InteractiveBackground;
