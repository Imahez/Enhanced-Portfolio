import React, { useEffect, useRef, useState } from 'react';
import usePrefersReducedMotion from '../../hooks/usePrefersReducedMotion';
import styles from './CustomCursor.module.css';

export function CustomCursor() {
  const dotRef = useRef(null);
  const ringRef = useRef(null);
  const prefersReducedMotion = usePrefersReducedMotion();

  const [mousePos, setMousePos] = useState({ x: -100, y: -100 });
  const [clicking, setClicking] = useState(false);
  const [hidden, setHidden] = useState(true);
  const [cursorState, setCursorState] = useState('default'); // 'default', 'expanded', 'magnetic', 'text'

  const lastCoords = useRef({ x: 0, y: 0 });
  const targetCoords = useRef({ x: 0, y: 0 });
  const magneticTarget = useRef(null);
  const isMagneticActive = useRef(false);

  useEffect(() => {
    // Only mount cursor on non-touch devices with fine pointers
    const mediaQuery = window.matchMedia('(hover: hover) and (pointer: fine)');
    if (!mediaQuery.matches || prefersReducedMotion) {
      document.body.style.cursor = 'default';
      return;
    }

    // Hide real cursor
    document.body.style.cursor = 'none';
    setHidden(false);

    const handleMouseMove = (e) => {
      setMousePos({ x: e.clientX, y: e.clientY });
      targetCoords.current = { x: e.clientX, y: e.clientY };

      if (isMagneticActive.current && magneticTarget.current) {
        const rect = magneticTarget.current.getBoundingClientRect();
        const centerX = rect.left + rect.width / 2;
        const centerY = rect.top + rect.height / 2;
        
        // Custom offset calculations
        const strength = 0.35;
        const dx = e.clientX - centerX;
        const dy = e.clientY - centerY;

        targetCoords.current = {
          x: centerX + dx * strength,
          y: centerY + dy * strength
        };

        // Apply visual offset pull on active target
        magneticTarget.current.style.transform = `translate3d(${dx * 0.12}px, ${dy * 0.12}px, 0)`;
      }
    };

    const handleMouseDown = () => setClicking(true);
    const handleMouseUp = () => setClicking(false);
    const handleMouseLeave = () => setHidden(true);
    const handleMouseEnter = () => setHidden(false);

    window.addEventListener('mousemove', handleMouseMove, { passive: true });
    window.addEventListener('mousedown', handleMouseDown);
    window.addEventListener('mouseup', handleMouseUp);
    document.body.addEventListener('mouseleave', handleMouseLeave);
    document.body.addEventListener('mouseenter', handleMouseEnter);

    // Dynamic state listener bindings on hoverable nodes
    const onMouseOver = (e) => {
      const target = e.target;
      if (!target) return;

      const mag = target.closest('button, .btn, [data-cursor="magnetic"]');
      const link = target.closest('a, [data-cursor="expand"]');
      const text = target.closest('p, li, .text-glow, [data-cursor="text"]');

      if (mag) {
        magneticTarget.current = mag;
        isMagneticActive.current = true;
        setCursorState('magnetic');
      } else if (link) {
        magneticTarget.current = null;
        isMagneticActive.current = false;
        setCursorState('expanded');
      } else if (text) {
        magneticTarget.current = null;
        isMagneticActive.current = false;
        setCursorState('text');
      }
    };

    const onMouseOut = (e) => {
      const target = e.target;
      if (!target) return;

      const mag = target.closest('button, .btn, [data-cursor="magnetic"]');
      if (mag) {
        mag.style.transform = '';
        mag.style.transition = 'transform 0.4s cubic-bezier(0.25, 0.46, 0.45, 0.94)';
        setTimeout(() => {
          mag.style.transition = '';
        }, 400);
      }

      setCursorState('default');
      isMagneticActive.current = false;
      magneticTarget.current = null;
    };

    document.addEventListener('mouseover', onMouseOver);
    document.addEventListener('mouseout', onMouseOut);

    return () => {
      document.body.style.cursor = 'default';
      window.removeEventListener('mousemove', handleMouseMove);
      window.removeEventListener('mousedown', handleMouseDown);
      window.removeEventListener('mouseup', handleMouseUp);
      document.body.removeEventListener('mouseleave', handleMouseLeave);
      document.body.removeEventListener('mouseenter', handleMouseEnter);
      document.removeEventListener('mouseover', onMouseOver);
      document.removeEventListener('mouseout', onMouseOut);
    };
  }, [prefersReducedMotion]);

  // Trail dots creation
  useEffect(() => {
    if (prefersReducedMotion || hidden) return;

    let count = 0;
    const spawnTrail = (e) => {
      count++;
      if (count % 2 !== 0) return; // limit frequency

      const trail = document.createElement('div');
      trail.className = 'react-trail-dot';
      trail.style.left = `${e.clientX}px`;
      trail.style.top = `${e.clientY}px`;
      const scaleVal = 0.3 + Math.random() * 0.7;
      trail.style.transform = `translate3d(-50%, -50%, 0) scale(${scaleVal})`;
      
      document.body.appendChild(trail);
      setTimeout(() => trail.remove(), 550);
    };

    window.addEventListener('mousemove', spawnTrail, { passive: true });
    return () => window.removeEventListener('mousemove', spawnTrail);
  }, [prefersReducedMotion, hidden]);

  // Eased follower loop for the ring
  useEffect(() => {
    if (prefersReducedMotion || hidden) return;

    let animId;
    const LERP_DEFAULT = 0.09;
    const LERP_MAGNETIC = 0.17;

    const animateFollower = () => {
      const lerpFactor = cursorState === 'magnetic' ? LERP_MAGNETIC : LERP_DEFAULT;
      lastCoords.current.x += (targetCoords.current.x - lastCoords.current.x) * lerpFactor;
      lastCoords.current.y += (targetCoords.current.y - lastCoords.current.y) * lerpFactor;

      if (ringRef.current) {
        ringRef.current.style.transform = `translate3d(${lastCoords.current.x.toFixed(2)}px, ${lastCoords.current.y.toFixed(2)}px, 0) translate3d(-50%, -50%, 0)`;
      }

      if (dotRef.current) {
        dotRef.current.style.transform = `translate3d(${mousePos.x}px, ${mousePos.y}px, 0) translate3d(-50%, -50%, 0)`;
      }

      animId = requestAnimationFrame(animateFollower);
    };

    animId = requestAnimationFrame(animateFollower);
    return () => cancelAnimationFrame(animId);
  }, [mousePos, cursorState, hidden, prefersReducedMotion]);

  if (hidden || prefersReducedMotion) return null;

  // Compute ring state classes
  const ringClass = [
    styles.ring,
    cursorState === 'expanded' ? styles.ringExpanded : '',
    cursorState === 'magnetic' ? styles.ringMagnetic : '',
    cursorState === 'text' ? styles.ringTextMode : '',
    hidden ? styles.hidden : ''
  ].join(' ');

  const dotClass = [
    styles.dot,
    clicking ? styles.dotClicking : '',
    hidden ? styles.hidden : ''
  ].join(' ');

  return (
    <>
      <div ref={dotRef} className={dotClass} />
      <div ref={ringRef} className={ringClass} />
    </>
  );
}
export default CustomCursor;
