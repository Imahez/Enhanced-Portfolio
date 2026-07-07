import React, { useRef, useState, useEffect } from 'react';
import usePrefersReducedMotion from '../../hooks/usePrefersReducedMotion';

export function Magnetic({ children, strength = 0.35, range = 50 }) {
  const ref = useRef(null);
  const prefersReducedMotion = usePrefersReducedMotion();
  const [position, setPosition] = useState({ x: 0, y: 0 });

  useEffect(() => {
    if (prefersReducedMotion) return;

    const el = ref.current;
    if (!el) return;

    const handleMouseMove = (e) => {
      const rect = el.getBoundingClientRect();
      const centerX = rect.left + rect.width / 2;
      const centerY = rect.top + rect.height / 2;

      // Distance from cursor to center
      const dx = e.clientX - centerX;
      const dy = e.clientY - centerY;
      const dist = Math.hypot(dx, dy);

      if (dist < range) {
        // Move element slightly toward cursor
        setPosition({
          x: dx * strength,
          y: dy * strength
        });
      } else {
        // Reset position
        setPosition({ x: 0, y: 0 });
      }
    };

    const handleMouseLeave = () => {
      setPosition({ x: 0, y: 0 });
    };

    window.addEventListener('mousemove', handleMouseMove, { passive: true });
    el.addEventListener('mouseleave', handleMouseLeave);

    return () => {
      window.removeEventListener('mousemove', handleMouseMove);
      if (el) el.removeEventListener('mouseleave', handleMouseLeave);
    };
  }, [strength, range, prefersReducedMotion]);

  const { x, y } = position;

  // Render wrapper component
  const styles = prefersReducedMotion 
    ? {} 
    : {
        transform: `translate3d(${x}px, ${y}px, 0)`,
        transition: x === 0 && y === 0 ? 'transform 0.4s cubic-bezier(0.25, 0.46, 0.45, 0.94)' : 'none'
      };

  return (
    <div 
      ref={ref} 
      style={{ display: 'inline-block', ...styles }} 
      data-cursor="magnetic"
    >
      {children}
    </div>
  );
}
export default Magnetic;
