#!/usr/bin/env python3
# Writes the complete premium Vercel/Linear redesigned portfolio to index.html
import os

CSS = """
:root{
  --bg:#000000;--bg-1:#050508;--bg-2:#0a0a12;
  --surface:rgba(255,255,255,0.03);--surface-2:rgba(255,255,255,0.055);
  --border:rgba(255,255,255,0.065);--border-2:rgba(255,255,255,0.12);--border-glow:rgba(124,58,237,0.5);
  --text:#ffffff;--text-2:#a1a1aa;--text-3:#52525b;
  --purple:#7c3aed;--purple-2:#6d28d9;--purple-light:#a78bfa;
  --blue:#2563eb;--blue-light:#60a5fa;--indigo:#4f46e5;--cyan:#22d3ee;--violet:#8b5cf6;
  --g-brand:linear-gradient(135deg,#7c3aed 0%,#4f46e5 50%,#2563eb 100%);
  --g-text:linear-gradient(135deg,#c4b5fd 10%,#818cf8 50%,#67e8f9 100%);
  --g-border:linear-gradient(135deg,rgba(124,58,237,0.6),rgba(79,70,229,0.4) 50%,rgba(37,99,235,0.5));
  --shadow-card:0 0 0 1px var(--border),0 8px 40px -8px rgba(0,0,0,0.8);
  --glow-purple:0 0 60px rgba(124,58,237,0.25),0 0 120px rgba(124,58,237,0.1);
  --glow-btn:0 0 20px rgba(124,58,237,0.6),0 0 40px rgba(124,58,237,0.3);
  --cursor-color:#7c3aed;
  --container:1160px;--nav-h:68px;
  --font:'Inter',system-ui,-apple-system,sans-serif;
  --font-mono:'JetBrains Mono',monospace;
  --r-sm:6px;--r:10px;--r-lg:14px;--r-xl:20px;--r-2xl:28px;
}
*,*::before,*::after{margin:0;padding:0;box-sizing:border-box}
html{scroll-behavior:smooth;font-size:16px}
body{font-family:var(--font);background:var(--bg);color:var(--text);line-height:1.6;overflow-x:hidden;-webkit-font-smoothing:antialiased}
a{color:inherit;text-decoration:none}
ul{list-style:none}
button{font-family:inherit;cursor:pointer}
img{max-width:100%;display:block}
::selection{background:rgba(124,58,237,0.4);color:#fff}
::-webkit-scrollbar{width:5px}
::-webkit-scrollbar-track{background:var(--bg)}
::-webkit-scrollbar-thumb{background:linear-gradient(var(--purple),var(--blue));border-radius:999px}
:focus-visible{outline:2px solid var(--purple);outline-offset:3px;border-radius:var(--r-sm)}
@media(prefers-reduced-motion:reduce){html{scroll-behavior:auto}*,*::before,*::after{animation-duration:0.001ms!important;transition-duration:0.001ms!important}}

/* Background */
body::after{content:'';position:fixed;inset:0;z-index:-3;
  background:radial-gradient(ellipse 80% 60% at 20% -10%,rgba(124,58,237,0.18) 0%,transparent 60%),
             radial-gradient(ellipse 60% 50% at 80% 110%,rgba(37,99,235,0.14) 0%,transparent 55%),
             radial-gradient(ellipse 50% 40% at 50% 50%,rgba(79,70,229,0.07) 0%,transparent 70%);
  pointer-events:none}
body::before{content:'';position:fixed;inset:0;z-index:1;pointer-events:none;opacity:0.025;
  background-image:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='250' height='250'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.8' numOctaves='4' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='250' height='250' filter='url(%23n)'/%3E%3C/svg%3E");
  background-size:180px}
#bg-canvas{position:fixed;inset:0;z-index:0;pointer-events:none}
.aurora{position:fixed;inset:0;z-index:0;pointer-events:none;overflow:hidden}
.aurora-blob{position:absolute;border-radius:50%;filter:blur(90px);will-change:transform;animation:auroraFloat var(--dur,20s) var(--delay,0s) ease-in-out infinite}
.aurora-blob:nth-child(1){width:680px;height:680px;top:-15%;left:-10%;background:radial-gradient(circle,rgba(124,58,237,0.28) 0%,transparent 70%);--dur:22s;--delay:0s}
.aurora-blob:nth-child(2){width:560px;height:560px;top:15%;right:-12%;background:radial-gradient(circle,rgba(37,99,235,0.22) 0%,transparent 70%);--dur:26s;--delay:-8s}
.aurora-blob:nth-child(3){width:720px;height:720px;bottom:-20%;left:20%;background:radial-gradient(circle,rgba(79,70,229,0.18) 0%,transparent 70%);--dur:30s;--delay:-15s}
.aurora-blob:nth-child(4){width:420px;height:420px;top:50%;left:55%;background:radial-gradient(circle,rgba(34,211,238,0.12) 0%,transparent 70%);--dur:18s;--delay:-5s}
@keyframes auroraFloat{0%,100%{transform:translate(0,0) scale(1)}25%{transform:translate(28px,-36px) scale(1.04)}50%{transform:translate(-18px,22px) scale(0.97)}75%{transform:translate(36px,12px) scale(1.02)}}
.bg-grid{position:fixed;inset:0;z-index:0;pointer-events:none;
  background-image:linear-gradient(rgba(255,255,255,0.03) 1px,transparent 1px),linear-gradient(90deg,rgba(255,255,255,0.03) 1px,transparent 1px);
  background-size:60px 60px;
  mask-image:radial-gradient(ellipse 85% 65% at 50% 0%,black 15%,transparent 80%);
  transform:translate(calc(var(--mx,0)*-6px),calc(var(--my,0)*-6px));transition:transform .12s linear}
#spotlight{position:fixed;inset:0;z-index:1;pointer-events:none;
  background:radial-gradient(700px circle at calc(var(--sx,50%)*1px) calc(var(--sy,50%)*1px),rgba(124,58,237,0.08) 0%,rgba(79,70,229,0.04) 40%,transparent 70%);
  mix-blend-mode:screen;opacity:0;transition:opacity .3s ease}
body.cursor-active #spotlight{opacity:1}

/* Cursor */
@media(hover:hover) and (pointer:fine){
  body.cursor-active,body.cursor-active *{cursor:none!important}
  #cursor-dot,#cursor-ring{position:fixed;top:0;left:0;border-radius:50%;pointer-events:none;z-index:99999;will-change:transform;
    transition:width .22s cubic-bezier(.25,.46,.45,.94),height .22s cubic-bezier(.25,.46,.45,.94),background .3s ease,border-color .3s ease,opacity .3s ease}
  #cursor-dot{width:7px;height:7px;background:var(--cursor-color,var(--purple));
    box-shadow:0 0 8px 3px var(--cursor-color,var(--purple)),0 0 20px 6px color-mix(in srgb,var(--cursor-color,var(--purple)) 45%,transparent);
    transform:translate(-50%,-50%)}
  #cursor-dot.clicking{transform:translate(-50%,-50%) scale(0.5);transition:transform .1s ease}
  #cursor-ring{width:38px;height:38px;border:1.5px solid var(--cursor-color,var(--purple));
    background:color-mix(in srgb,var(--cursor-color,var(--purple)) 5%,transparent);
    transform:translate(-50%,-50%);mix-blend-mode:exclusion}
  #cursor-ring.expanded{width:62px;height:62px;border-width:1px}
  #cursor-ring.magnetic{width:50px;height:50px;border-width:2px;background:color-mix(in srgb,var(--cursor-color,var(--purple)) 15%,transparent)}
  #cursor-ring.text-mode{width:3px;height:34px;border-radius:2px;border-width:0;background:var(--cursor-color,var(--purple));opacity:.7}
  #cursor-dot.hidden,#cursor-ring.hidden{opacity:0}
  .trail-dot{position:fixed;width:5px;height:5px;border-radius:50%;pointer-events:none;z-index:99998;
    transform:translate(-50%,-50%);background:var(--cursor-color,var(--purple));
    box-shadow:0 0 6px 2px var(--cursor-color,var(--purple));animation:trailFade .55s cubic-bezier(.4,0,.2,1) forwards}
  @keyframes trailFade{from{opacity:.65;transform:translate(-50%,-50%) scale(1)}to{opacity:0;transform:translate(-50%,-50%) scale(.08)}}
}

/* Scroll progress */
#scroll-progress{position:fixed;top:0;left:0;height:2px;width:0%;background:var(--g-brand);z-index:99999;pointer-events:none;
  box-shadow:0 0 10px rgba(124,58,237,0.8);transition:width .1s linear}

/* Nav */
header{position:fixed;top:0;left:0;right:0;z-index:100;border-bottom:1px solid transparent;
  transition:background .4s ease,border-color .4s ease,backdrop-filter .4s ease}
header.scrolled{background:rgba(0,0,0,0.75);backdrop-filter:blur(20px) saturate(1.5);-webkit-backdrop-filter:blur(20px) saturate(1.5);border-bottom-color:var(--border)}
nav{max-width:var(--container);margin:0 auto;padding:0 24px;height:var(--nav-h);display:flex;align-items:center;justify-content:space-between}
.nav-logo{display:flex;align-items:center;gap:10px;font-weight:700;font-size:1rem;letter-spacing:-.02em}
.nav-logo-icon{width:32px;height:32px;border-radius:8px;background:var(--g-brand);display:flex;align-items:center;justify-content:center;
  font-family:var(--font-mono);font-weight:700;font-size:.9rem;color:#fff;box-shadow:0 0 16px rgba(124,58,237,0.5)}
.nav-links{display:flex;align-items:center;gap:6px}
.nav-links a{font-size:.85rem;font-weight:500;color:var(--text-2);padding:6px 12px;border-radius:var(--r);transition:color .2s ease,background .2s ease}
.nav-links a:hover{color:var(--text);background:var(--surface)}
.nav-links a.active{color:var(--text)}
.nav-actions{display:flex;align-items:center;gap:10px}
.nav-pill{display:flex;align-items:center;gap:7px;font-size:.8rem;font-weight:600;padding:7px 14px;border-radius:999px;
  background:var(--surface-2);border:1px solid var(--border-2);color:var(--text-2);transition:all .2s ease}
.nav-pill:hover{color:var(--text);border-color:var(--border-glow)}
.nav-pill .pulse{width:6px;height:6px;border-radius:50%;background:#22c55e;box-shadow:0 0 8px #22c55e;animation:pulse 2s ease infinite}
@keyframes pulse{0%,100%{opacity:1}50%{opacity:.4}}
.nav-resume{padding:8px 16px;border-radius:var(--r);background:var(--g-brand);font-size:.82rem;font-weight:600;color:#fff;border:none;
  box-shadow:0 0 20px rgba(124,58,237,0.4);transition:transform .2s ease,box-shadow .2s ease;display:inline-block}
.nav-resume:hover{transform:translateY(-1px);box-shadow:0 0 30px rgba(124,58,237,0.6)}
.nav-burger{display:none;width:36px;height:36px;border-radius:var(--r);background:var(--surface);border:1px solid var(--border);align-items:center;justify-content:center;color:var(--text-2)}
@media(max-width:860px){.nav-links,.nav-pill{display:none}.nav-burger{display:flex}}
.mobile-nav{position:fixed;top:var(--nav-h);left:0;right:0;z-index:99;background:rgba(0,0,0,0.9);backdrop-filter:blur(20px);
  border-bottom:1px solid var(--border);padding:16px 24px;display:flex;flex-direction:column;gap:4px;
  transform:translateY(-110%);opacity:0;transition:all .3s cubic-bezier(.4,0,.2,1)}
.mobile-nav.open{transform:translateY(0);opacity:1}
.mobile-nav a{padding:12px 16px;border-radius:var(--r);font-weight:500;color:var(--text-2);transition:color .2s ease,background .2s ease}
.mobile-nav a:hover{color:var(--text);background:var(--surface)}

/* Layout */
.container{max-width:var(--container);margin:0 auto;padding:0 24px}
section{position:relative;z-index:2;padding:120px 0}
section#home{padding:0}

/* Labels + headings */
.s-label{display:inline-flex;align-items:center;gap:8px;font-size:.72rem;font-weight:700;letter-spacing:.1em;text-transform:uppercase;color:var(--purple-light);margin-bottom:18px}
.s-label::before{content:'';width:18px;height:1px;background:var(--purple-light)}
.s-title{font-size:clamp(2rem,4.5vw,3.2rem);font-weight:800;letter-spacing:-.03em;line-height:1.1;margin-bottom:18px}
.s-sub{font-size:1.05rem;color:var(--text-2);line-height:1.75;max-width:580px;margin-bottom:60px}

/* Gradient text */
.grad-text{background:var(--g-text);-webkit-background-clip:text;background-clip:text;-webkit-text-fill-color:transparent;text-fill-color:transparent;background-size:200% 100%;animation:gradShift 6s ease-in-out infinite alternate}
@keyframes gradShift{from{background-position:0% 50%}to{background-position:100% 50%}}

/* Reveal */
.reveal{opacity:0;transform:translateY(30px);transition:opacity .8s cubic-bezier(.2,.8,.2,1),transform .8s cubic-bezier(.2,.8,.2,1)}
.reveal-left{opacity:0;transform:translateX(-40px);transition:opacity .8s cubic-bezier(.2,.8,.2,1),transform .8s cubic-bezier(.2,.8,.2,1)}
.reveal-right{opacity:0;transform:translateX(40px);transition:opacity .8s cubic-bezier(.2,.8,.2,1),transform .8s cubic-bezier(.2,.8,.2,1)}
.reveal-scale{opacity:0;transform:scale(.93);transition:opacity .7s cubic-bezier(.2,.8,.2,1),transform .7s cubic-bezier(.2,.8,.2,1)}
.reveal.in,.reveal-left.in,.reveal-right.in,.reveal-scale.in{opacity:1;transform:none}
.stagger > *{opacity:0;transform:translateY(22px);transition:opacity .6s cubic-bezier(.2,.8,.2,1),transform .6s cubic-bezier(.2,.8,.2,1)}
.stagger.in > *:nth-child(1){transition-delay:.04s}
.stagger.in > *:nth-child(2){transition-delay:.1s}
.stagger.in > *:nth-child(3){transition-delay:.16s}
.stagger.in > *:nth-child(4){transition-delay:.22s}
.stagger.in > *:nth-child(5){transition-delay:.28s}
.stagger.in > *:nth-child(6){transition-delay:.34s}
.stagger.in > *{opacity:1;transform:none}

/* Glass card */
.glass{background:rgba(255,255,255,0.03);backdrop-filter:blur(16px) saturate(1.6);-webkit-backdrop-filter:blur(16px) saturate(1.6);
  border:1px solid var(--border);border-radius:var(--r-xl);position:relative;transition:border-color .3s ease,box-shadow .3s ease,transform .3s ease}
.glass:hover{border-color:rgba(124,58,237,0.35);box-shadow:0 0 0 1px rgba(124,58,237,0.15),0 20px 60px -20px rgba(0,0,0,0.7),var(--glow-purple)}
.glass::before{content:'';position:absolute;inset:0;border-radius:inherit;padding:1px;background:var(--g-border);
  -webkit-mask:linear-gradient(#fff 0 0) content-box,linear-gradient(#fff 0 0);mask:linear-gradient(#fff 0 0) content-box,linear-gradient(#fff 0 0);
  -webkit-mask-composite:xor;mask-composite:exclude;pointer-events:none;opacity:0;transition:opacity .35s ease}
.glass:hover::before{opacity:0.7}

/* Buttons */
.btn{display:inline-flex;align-items:center;gap:8px;font-weight:600;font-size:.9rem;border-radius:var(--r);padding:12px 22px;border:none;cursor:pointer;
  transition:transform .2s ease,box-shadow .2s ease;position:relative;overflow:hidden;isolation:isolate;font-family:var(--font);text-decoration:none}
.btn::after{content:'';position:absolute;top:0;left:-100%;width:55%;height:100%;
  background:linear-gradient(105deg,transparent 30%,rgba(255,255,255,0.4) 50%,transparent 70%);transform:skewX(-18deg);pointer-events:none}
.btn:hover::after{animation:btnShimmer .5s ease forwards}
@keyframes btnShimmer{from{left:-100%}to{left:160%}}
.btn:hover{transform:translateY(-2px)}
.btn-primary{background:var(--g-brand);color:#fff;box-shadow:0 0 24px rgba(124,58,237,0.45),0 4px 16px rgba(0,0,0,0.4)}
.btn-primary:hover{box-shadow:0 0 36px rgba(124,58,237,0.7),0 8px 24px rgba(0,0,0,0.5)}
.btn-ghost{background:var(--surface);color:var(--text-2);border:1px solid var(--border-2)}
.btn-ghost:hover{color:var(--text);border-color:rgba(124,58,237,0.5);background:rgba(124,58,237,0.08)}

/* Hero */
.hero{min-height:100vh;display:flex;align-items:center;padding-top:var(--nav-h)}
.hero-inner{display:grid;grid-template-columns:1.1fr 1fr;gap:64px;align-items:center;padding:60px 0}
@media(max-width:900px){.hero-inner{grid-template-columns:1fr;gap:48px}}
.hero-badge{display:inline-flex;align-items:center;gap:8px;font-size:.78rem;font-weight:600;letter-spacing:.04em;padding:6px 14px 6px 8px;border-radius:999px;
  background:rgba(124,58,237,0.1);border:1px solid rgba(124,58,237,0.3);color:var(--purple-light);margin-bottom:28px}
.hero-badge .pulse{width:7px;height:7px;border-radius:50%;background:#22c55e;box-shadow:0 0 8px #22c55e;animation:pulse 2s ease infinite}
.hero h1{font-size:clamp(2.6rem,5.5vw,4.2rem);font-weight:800;letter-spacing:-.04em;line-height:1.08;margin-bottom:24px}
.hero-lead{font-size:1.1rem;color:var(--text-2);line-height:1.75;max-width:500px;margin-bottom:36px}
.hero-cta{display:flex;gap:12px;flex-wrap:wrap;margin-bottom:40px}
.hero-socials{display:flex;gap:10px}
.hero-socials a{width:40px;height:40px;border-radius:var(--r);background:var(--surface);border:1px solid var(--border);
  display:flex;align-items:center;justify-content:center;color:var(--text-3);transition:all .25s ease}
.hero-socials a:hover{color:var(--purple-light);border-color:rgba(124,58,237,0.45);background:rgba(124,58,237,0.08);transform:translateY(-2px)}
.star{position:absolute;border-radius:50%;background:rgba(255,255,255,0.8);pointer-events:none;animation:twinkle var(--dur,3s) var(--delay,0s) ease-in-out infinite}
@keyframes twinkle{0%,100%{opacity:var(--max,.5)}50%{opacity:.04}}

/* IDE card */
.ide-card{background:rgba(3,3,12,0.9);border:1px solid var(--border);border-radius:var(--r-xl);overflow:hidden;
  box-shadow:var(--shadow-card),var(--glow-purple)}
.ide-bar{display:flex;align-items:center;gap:6px;padding:12px 16px;background:rgba(255,255,255,0.025);border-bottom:1px solid var(--border)}
.ide-dot{width:11px;height:11px;border-radius:50%}
.ide-tab-row{margin-left:14px}
.ide-tab{font-family:var(--font-mono);font-size:.72rem;color:var(--text-3);padding:5px 12px;border-radius:6px 6px 0 0;
  background:rgba(255,255,255,0.04);border:1px solid var(--border);border-bottom:none}
.ide-body{padding:20px 22px;font-family:var(--font-mono);font-size:.8rem;line-height:1.75;min-height:240px;color:#e2e2e2}
.ln{color:var(--text-3);display:inline-block;width:22px;user-select:none}
.kw{color:#c792ea}.cls{color:#82aaff}.str{color:#c3e88d}.cmt{color:#546e7a}.fn{color:#a78bfa}
.terminal-box{border-top:1px solid var(--border);background:#010108;padding:14px 22px;font-family:var(--font-mono);font-size:.78rem;color:#86efac;min-height:70px;cursor:text}
.t-prompt{color:var(--purple-light);font-weight:700}
.t-cwd{color:var(--text-3);margin-right:6px}
#terminalLog{margin-bottom:6px;max-height:140px;overflow-y:auto}
#terminalLog .line{line-height:1.7}
#terminalLog .echo{color:var(--text-3)}
#terminalLog .echo::before{content:'-> ~ ';color:var(--purple-light)}
#terminalLog .out{color:#86efac}
#terminalLog .dim{color:var(--text-3)}
#terminalLog .hl{color:var(--purple-light)}
.t-row{display:flex;align-items:center;position:relative}
.t-input{background:transparent;border:none;outline:none;color:#86efac;font-family:var(--font-mono);font-size:.78rem;flex:1;caret-color:transparent;padding:0;margin-left:2px}
#termTypedHint{color:var(--text-3);position:absolute;opacity:0;pointer-events:none}
.t-cursor{display:inline-block;width:6px;height:14px;background:#86efac;margin-left:1px;flex-shrink:0;animation:blink 1s step-end infinite}
.t-input:focus + .t-cursor{background:var(--purple-light)}
@keyframes blink{0%,100%{opacity:1}50%{opacity:0}}

/* About */
.about-grid{display:grid;grid-template-columns:300px 1fr;gap:64px;align-items:start}
@media(max-width:860px){.about-grid{grid-template-columns:1fr}}
.about-photo-wrap{position:relative;border-radius:var(--r-xl);overflow:hidden;aspect-ratio:3/4;cursor:pointer;max-width:300px}
.about-photo{width:100%;height:100%;object-fit:cover;filter:grayscale(1) contrast(1.1);transition:filter .6s ease}
.about-photo-tint{position:absolute;inset:0;background:linear-gradient(150deg,rgba(124,58,237,0.55) 0%,rgba(37,99,235,0.4) 100%);mix-blend-mode:color;opacity:.9;transition:opacity .6s ease;pointer-events:none}
.about-photo-wrap:hover .about-photo{filter:grayscale(0) contrast(1)}
.about-photo-wrap:hover .about-photo-tint{opacity:0}
.about-border{position:absolute;inset:-1px;border-radius:inherit;padding:2px;background:var(--g-brand);
  -webkit-mask:linear-gradient(#fff 0 0) content-box,linear-gradient(#fff 0 0);mask:linear-gradient(#fff 0 0) content-box,linear-gradient(#fff 0 0);
  -webkit-mask-composite:xor;mask-composite:exclude;pointer-events:none}
.about-photo-hint{position:absolute;bottom:0;left:0;right:0;padding:40px 16px 16px;
  background:linear-gradient(transparent,rgba(0,0,0,0.75));font-size:.72rem;font-family:var(--font-mono);color:rgba(255,255,255,0.7);
  text-align:center;pointer-events:none;transition:opacity .3s ease}
.about-photo-wrap:hover .about-photo-hint{opacity:0}
.about-text p{color:var(--text-2);line-height:1.85;font-size:1rem;margin-bottom:18px}
.about-text strong{color:var(--text)}
.stat-row{display:grid;grid-template-columns:repeat(auto-fit,minmax(110px,1fr));gap:14px;margin-top:32px}
.stat-card{padding:18px 16px;border-radius:var(--r-lg);background:var(--surface);border:1px solid var(--border);text-align:center;transition:all .3s ease}
.stat-card:hover{border-color:rgba(124,58,237,0.4);background:rgba(124,58,237,0.06)}
.stat-num{font-size:1.8rem;font-weight:800;font-family:var(--font-mono)}
.stat-label{font-size:.72rem;color:var(--text-3);text-transform:uppercase;letter-spacing:.05em;margin-top:4px}

/* Skills */
.skills-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:16px}
@media(max-width:860px){.skills-grid{grid-template-columns:1fr 1fr}}
@media(max-width:560px){.skills-grid{grid-template-columns:1fr}}
.skill-card{padding:26px 24px;border-radius:var(--r-xl);background:var(--surface);border:1px solid var(--border);
  transition:all .3s cubic-bezier(.25,.46,.45,.94);position:relative;overflow:hidden;isolation:isolate}
.skill-card:hover{border-color:rgba(124,58,237,0.35);transform:translateY(-4px);box-shadow:0 0 0 1px rgba(124,58,237,0.1),0 20px 40px -12px rgba(0,0,0,0.6)}
.skill-icon{width:40px;height:40px;border-radius:var(--r);background:rgba(124,58,237,0.15);border:1px solid rgba(124,58,237,0.25);
  display:flex;align-items:center;justify-content:center;font-size:1.1rem;margin-bottom:14px;transition:box-shadow .3s ease}
.skill-card:hover .skill-icon{box-shadow:0 0 20px rgba(124,58,237,0.4)}
.skill-cat{font-size:.7rem;font-weight:700;letter-spacing:.08em;text-transform:uppercase;color:var(--purple-light);margin-bottom:10px}
.skill-name{font-weight:700;font-size:1.05rem;margin-bottom:12px}
.skill-tags-row{display:flex;flex-wrap:wrap;gap:6px}
.skill-tag{font-size:.72rem;font-weight:600;padding:4px 10px;border-radius:999px;background:rgba(255,255,255,0.05);color:var(--text-2);border:1px solid var(--border)}

/* Projects */
.projects-grid{display:grid;grid-template-columns:1fr 1fr;gap:20px}
@media(max-width:860px){.projects-grid{grid-template-columns:1fr}}
.project-card{border-radius:var(--r-xl);overflow:hidden;display:flex;flex-direction:column;background:var(--surface);border:1px solid var(--border);
  transition:all .35s cubic-bezier(.25,.46,.45,.94);position:relative}
.project-card:hover{border-color:rgba(124,58,237,0.4);transform:translateY(-6px);box-shadow:0 0 0 1px rgba(124,58,237,0.12),0 24px 60px -16px rgba(0,0,0,0.8),var(--glow-purple)}
.project-card::before{content:'';position:absolute;top:0;left:0;right:0;height:2px;background:var(--g-brand);opacity:0;transition:opacity .35s ease}
.project-card:hover::before{opacity:1}
.project-visual{height:190px;position:relative;overflow:hidden;
  background:repeating-linear-gradient(135deg,transparent 0 20px,rgba(124,58,237,0.04) 20px 21px) rgba(124,58,237,0.03);
  border-bottom:1px solid var(--border);display:flex;align-items:center;justify-content:center}
.p-stat{position:absolute;bottom:12px;left:12px;font-family:var(--font-mono);font-size:.7rem;
  background:rgba(0,0,0,0.6);border:1px solid rgba(124,58,237,0.3);color:var(--purple-light);padding:4px 10px;border-radius:6px}
.cal-grid{display:flex;flex-direction:column;gap:6px}
.cal-row{display:flex;gap:6px}
.cal-cell{width:30px;height:24px;border-radius:5px;background:rgba(124,58,237,0.08);border:1px solid rgba(124,58,237,0.2);overflow:hidden;position:relative}
.cal-fill{position:absolute;inset:0;background:linear-gradient(135deg,#7c3aed,#2563eb);transform:scaleX(0);transform-origin:left;animation:fillCell 3.6s ease-in-out infinite}
.cal-cell:nth-child(1) .cal-fill{animation-delay:.1s}
.cal-cell:nth-child(2) .cal-fill{animation-delay:.5s}
.cal-cell:nth-child(3) .cal-fill{animation-delay:.9s}
.cal-cell:nth-child(4) .cal-fill{animation-delay:1.3s}
@keyframes fillCell{0%{transform:scaleX(0)}35%{transform:scaleX(1)}70%{transform:scaleX(1)}90%{transform:scaleX(0);opacity:.5}100%{transform:scaleX(0);opacity:1}}
.cal-cap{margin-top:10px;font-family:var(--font-mono);font-size:.65rem;color:var(--text-3);text-align:center}
.cal-cap b{color:var(--purple-light)}
.route-wrap{width:160px;height:80px;position:relative}
.route-wrap svg{width:100%;height:100%;overflow:visible}
.route-path{fill:none;stroke:url(#rg2);stroke-width:2;stroke-dasharray:6 5;stroke-dashoffset:0;animation:dashAnim 1.5s linear infinite}
@keyframes dashAnim{to{stroke-dashoffset:-22}}
.route-pin{fill:var(--purple-light)}
.route-cap{position:absolute;bottom:-4px;left:0;right:0;text-align:center;font-family:var(--font-mono);font-size:.65rem;color:var(--text-3)}
.route-cap b{color:var(--blue-light)}
.project-body{padding:24px;display:flex;flex-direction:column;flex:1}
.project-num{font-size:.7rem;font-weight:700;letter-spacing:.08em;color:var(--text-3);text-transform:uppercase;margin-bottom:8px}
.project-name{font-size:1.3rem;font-weight:800;letter-spacing:-.02em;margin-bottom:10px}
.project-desc{color:var(--text-2);font-size:.9rem;line-height:1.65;margin-bottom:18px}
.project-tags{display:flex;flex-wrap:wrap;gap:6px;margin-bottom:20px}
.project-tag{font-size:.7rem;font-weight:600;padding:4px 10px;border-radius:999px;background:rgba(124,58,237,0.1);color:var(--purple-light);border:1px solid rgba(124,58,237,0.2)}
.project-links{margin-top:auto;display:flex;gap:10px;align-items:center}
.p-link{display:inline-flex;align-items:center;gap:6px;font-size:.82rem;font-weight:600;color:var(--text-2);
  padding:7px 14px;border-radius:var(--r);background:var(--surface);border:1px solid var(--border);transition:all .2s ease;font-family:var(--font)}
.p-link:hover{color:var(--text);border-color:rgba(124,58,237,0.5);background:rgba(124,58,237,0.08)}
.p-link.primary{background:rgba(124,58,237,0.15);border-color:rgba(124,58,237,0.3);color:var(--purple-light)}
.p-link.primary:hover{background:rgba(124,58,237,0.25)}
button.p-link{cursor:pointer}

/* Modal */
.modal-overlay{position:fixed;inset:0;z-index:500;background:rgba(0,0,0,0.8);backdrop-filter:blur(8px);display:none;align-items:center;justify-content:center;padding:24px}
.modal-overlay.open{display:flex}
.modal-box{background:#0a0a12;border:1px solid var(--border);border-radius:var(--r-xl);max-width:600px;width:100%;max-height:85vh;overflow-y:auto;padding:36px;box-shadow:var(--glow-purple)}
.modal-close{float:right;background:var(--surface);border:1px solid var(--border);width:32px;height:32px;border-radius:var(--r);color:var(--text-2);font-size:.9rem;transition:all .2s ease;cursor:pointer}
.modal-close:hover{color:var(--text);border-color:var(--border-2)}
.modal-box h3{font-size:1.4rem;font-weight:800;margin-bottom:8px}
.modal-tags{display:flex;flex-wrap:wrap;gap:6px;margin:14px 0}
.modal-box ul li{color:var(--text-2);font-size:.93rem;line-height:1.75;padding-left:20px;position:relative;margin-bottom:10px}
.modal-box ul li::before{content:'>';position:absolute;left:0;color:var(--purple-light);font-weight:800}

/* Experience */
.timeline{position:relative;padding-left:36px}
.timeline::before{content:'';position:absolute;left:0;top:0;bottom:0;width:2px;background:var(--border)}
.timeline::after{content:'';position:absolute;left:0;top:0;width:2px;height:calc(var(--tl,0)*100%);background:var(--g-brand);transition:height .12s linear}
.timeline-item{position:relative;padding-bottom:12px}
.timeline-item::before{content:'';position:absolute;left:-42px;top:6px;width:14px;height:14px;border-radius:50%;
  background:var(--g-brand);border:3px solid var(--bg);
  box-shadow:0 0 0 2px var(--purple),0 0 16px rgba(124,58,237,0.6);animation:dotGlow 2.5s ease-in-out infinite}
@keyframes dotGlow{0%,100%{box-shadow:0 0 0 2px var(--purple)}50%{box-shadow:0 0 0 6px rgba(124,58,237,0.2),0 0 0 2px var(--purple)}}
.exp-card{padding:28px 30px;border-radius:var(--r-xl)}
.exp-top{display:flex;justify-content:space-between;flex-wrap:wrap;gap:10px;align-items:flex-start;margin-bottom:6px}
.exp-role{font-weight:800;font-size:1.1rem}
.exp-date{font-family:var(--font-mono);font-size:.75rem;background:rgba(124,58,237,0.12);border:1px solid rgba(124,58,237,0.25);color:var(--purple-light);padding:4px 12px;border-radius:999px}
.exp-company{color:var(--blue-light);font-weight:600;font-size:.92rem;margin-bottom:18px}
.exp-list li{color:var(--text-2);font-size:.92rem;line-height:1.7;padding-left:20px;position:relative;margin-bottom:9px}
.exp-list li::before{content:'>';position:absolute;left:0;color:var(--purple-light);font-weight:700}

/* Certs + Education */
.split-grid{display:grid;grid-template-columns:1.4fr 1fr;gap:24px}
@media(max-width:860px){.split-grid{grid-template-columns:1fr}}
.cert-list{display:flex;flex-direction:column;gap:12px}
.cert-card{display:flex;align-items:center;gap:16px;padding:18px 20px;border-radius:var(--r-xl);background:var(--surface);border:1px solid var(--border);transition:all .3s ease}
.cert-card:hover{border-color:rgba(124,58,237,0.4);background:rgba(124,58,237,0.05)}
.cert-ico{width:40px;height:40px;flex-shrink:0;border-radius:var(--r);background:rgba(124,58,237,0.15);border:1px solid rgba(124,58,237,0.25);display:flex;align-items:center;justify-content:center;color:var(--purple-light)}
.cert-card h4{font-size:.94rem;font-weight:700;margin-bottom:3px}
.cert-card span{font-size:.78rem;color:var(--text-3)}
.edu-card{padding:28px;border-radius:var(--r-xl);height:fit-content}
.edu-card h4{font-weight:800;font-size:1.05rem;margin-bottom:6px}
.edu-inst{color:var(--blue-light);font-weight:600;font-size:.9rem;margin-bottom:18px}
.edu-row{display:flex;justify-content:space-between;font-size:.85rem;padding:10px 0;border-top:1px solid var(--border);color:var(--text-3)}
.edu-row b{color:var(--text)}

/* Contact */
.contact-grid{display:grid;grid-template-columns:1fr 1.2fr;gap:40px}
@media(max-width:860px){.contact-grid{grid-template-columns:1fr}}
.contact-info{display:flex;flex-direction:column;gap:16px}
.contact-item{display:flex;align-items:flex-start;gap:14px;padding:16px 18px;border-radius:var(--r-xl);background:var(--surface);border:1px solid var(--border);cursor:pointer;transition:all .25s ease}
.contact-item:hover{border-color:rgba(124,58,237,0.4);background:rgba(124,58,237,0.05)}
.contact-ico{width:40px;height:40px;flex-shrink:0;border-radius:var(--r);background:rgba(124,58,237,0.15);border:1px solid rgba(124,58,237,0.25);display:flex;align-items:center;justify-content:center;color:var(--purple-light)}
.contact-item h4{font-size:.73rem;text-transform:uppercase;letter-spacing:.06em;color:var(--text-3);margin-bottom:3px}
.contact-item p{font-weight:600;font-size:.95rem}
.form-card{padding:32px;border-radius:var(--r-xl)}
.form-row{margin-bottom:18px}
.form-row label{display:block;font-size:.78rem;font-weight:600;color:var(--text-3);margin-bottom:8px;text-transform:uppercase;letter-spacing:.04em}
.form-row input,.form-row textarea{width:100%;background:rgba(255,255,255,0.03);border:1px solid var(--border);border-radius:var(--r);padding:12px 16px;color:var(--text);font-family:var(--font);font-size:.92rem;transition:border-color .2s ease,box-shadow .2s ease}
.form-row input:focus,.form-row textarea:focus{outline:none;border-color:rgba(124,58,237,0.6);box-shadow:0 0 0 3px rgba(124,58,237,0.12),0 0 20px -5px rgba(124,58,237,0.2)}
.form-row textarea{resize:vertical;min-height:115px}
.form-row input::placeholder,.form-row textarea::placeholder{color:var(--text-3)}
.submit-btn{width:100%;background:var(--g-brand);color:#fff;font-weight:700;padding:14px;border-radius:var(--r);border:none;font-size:.95rem;
  display:flex;align-items:center;justify-content:center;gap:8px;transition:transform .2s ease,box-shadow .2s ease;
  position:relative;overflow:hidden;cursor:pointer;font-family:var(--font)}
.submit-btn::after{content:'';position:absolute;top:0;left:-100%;width:55%;height:100%;background:linear-gradient(105deg,transparent 30%,rgba(255,255,255,0.4) 50%,transparent 70%);transform:skewX(-18deg);pointer-events:none}
.submit-btn:hover::after{animation:btnShimmer .5s ease forwards}
.submit-btn:hover{transform:translateY(-2px);box-shadow:var(--glow-btn)}
.submit-btn:disabled{opacity:.6;cursor:not-allowed;transform:none}
.form-msg{margin-top:14px;font-size:.85rem;font-weight:600;display:none;padding:10px 14px;border-radius:var(--r)}
.form-msg.ok{display:block;background:rgba(34,197,94,.12);color:#4ade80;border:1px solid rgba(34,197,94,.25)}
.form-msg.err{display:block;background:rgba(239,68,68,.12);color:#f87171;border:1px solid rgba(239,68,68,.25)}

/* Footer */
footer{position:relative;z-index:2;border-top:1px solid var(--border);padding:40px 0}
.footer-inner{display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:16px}
.footer-copy{font-size:.82rem;color:var(--text-3);font-family:var(--font-mono)}
.footer-copy a{color:var(--purple-light);transition:color .2s ease}
.footer-copy a:hover{color:var(--text)}
.back-top{width:40px;height:40px;border-radius:var(--r);background:var(--surface);border:1px solid var(--border);display:flex;align-items:center;justify-content:center;color:var(--text-2);transition:all .25s ease}
.back-top:hover{color:var(--text);border-color:rgba(124,58,237,0.4)}
.divider{height:1px;background:linear-gradient(90deg,transparent,rgba(124,58,237,0.3) 25%,rgba(79,70,229,0.3) 50%,rgba(37,99,235,0.25) 75%,transparent);border:none;margin:0}
.tilt{transform-style:preserve-3d;transform:perspective(1200px);transition:transform .1s linear;will-change:transform}
"""

HTML = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8"/>
<meta name="viewport" content="width=device-width,initial-scale=1.0"/>
<meta name="robots" content="index,follow"/>
<title>Sreemaheshkumar S - Full Stack Java and React Developer</title>
<meta name="description" content="Sreemaheshkumar S is a full-stack developer specialising in Java, Spring Boot, and React.js. Builder of MedVault and EcoWaste."/>
<meta property="og:title" content="Sreemaheshkumar S - Full Stack Developer"/>
<meta property="og:type" content="website"/>
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 64 64'%3E%3Crect width='64' height='64' rx='16' fill='%237c3aed'/%3E%3Ctext x='50%25' y='55%25' dominant-baseline='middle' text-anchor='middle' font-family='Georgia,serif' font-size='36' font-weight='bold' fill='white'%3EM%3C/text%3E%3C/svg%3E"/>
<link rel="preconnect" href="https://fonts.googleapis.com"/>
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin/>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&family=JetBrains+Mono:wght@400;500;600;700&display=swap" rel="stylesheet"/>
<script src="https://cdn.jsdelivr.net/npm/@emailjs/browser@4/dist/email.min.js"></script>
<script>(function(){emailjs.init({publicKey:'Lr0xd2FOJ01UNMZhU'});})()</script>
<style>CSS_PLACEHOLDER</style>
</head>
<body>
<canvas id="bg-canvas" aria-hidden="true"></canvas>
<div class="aurora" aria-hidden="true"><div class="aurora-blob"></div><div class="aurora-blob"></div><div class="aurora-blob"></div><div class="aurora-blob"></div></div>
<div class="bg-grid" aria-hidden="true"></div>
<div id="spotlight" aria-hidden="true"></div>
<div id="cursor-dot" aria-hidden="true"></div>
<div id="cursor-ring" aria-hidden="true"></div>
<div id="scroll-progress" aria-hidden="true"></div>

<header id="site-header">
<nav>
  <a href="#home" class="nav-logo">
    <div class="nav-logo-icon">M</div>
    <span>mahesh<span style="color:var(--text-3)">.dev</span></span>
  </a>
  <div class="nav-links">
    <a href="#about">About</a><a href="#skills">Skills</a>
    <a href="#experience">Experience</a><a href="#projects">Projects</a><a href="#contact">Contact</a>
  </div>
  <div class="nav-actions">
    <div class="nav-pill"><span class="pulse"></span>Available for hire</div>
    <a class="nav-resume" href="resume.pdf" download="Sreemaheshkumar_S_Resume.pdf">Resume &darr;</a>
    <button class="nav-burger" id="burgerBtn" aria-label="Open menu">
      <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
        <line x1="3" y1="6" x2="21" y2="6"/><line x1="3" y1="12" x2="21" y2="12"/><line x1="3" y1="18" x2="21" y2="18"/>
      </svg>
    </button>
  </div>
</nav>
</header>
<div class="mobile-nav" id="mobileNav">
  <a href="#about">About</a><a href="#skills">Skills</a>
  <a href="#experience">Experience</a><a href="#projects">Projects</a>
  <a href="#certifications">Certifications</a><a href="#contact">Contact</a>
</div>

<section id="home" class="hero" style="overflow:hidden;position:relative;">
<div class="container">
<div class="hero-inner">
  <div>
    <div class="hero-badge reveal"><span class="pulse"></span>Open to Software Developer roles</div>
    <h1 class="reveal" style="transition-delay:.1s">
      <span id="hl1" class="decode-line" data-final="Sreemaheshkumar S"></span><br>
      <span id="hl2" class="decode-line" data-final="builds full-stack" style="color:var(--text-2)"></span><br>
      <span id="hl3" class="decode-line grad-text" data-final="systems in Java &amp; React."></span>
    </h1>
    <p class="hero-lead reveal" style="transition-delay:.2s">CS fresher with production-grade experience shipping secure, role-based platforms &mdash; from JWT-authenticated healthcare systems to geolocation-powered logistics tools.</p>
    <div class="hero-cta reveal" style="transition-delay:.3s">
      <a href="#projects" class="btn btn-primary">View Projects &rarr;</a>
      <a href="#contact" class="btn btn-ghost">Get In Touch</a>
    </div>
    <div class="hero-socials reveal" style="transition-delay:.4s">
      <a href="https://github.com/Imahez" target="_blank" rel="noopener" aria-label="GitHub">
        <svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor"><path d="M12 .5C5.73.5.5 5.74.5 12.02c0 5.02 3.26 9.28 7.78 10.79.57.1.78-.25.78-.55v-2.14c-3.17.69-3.83-1.36-3.83-1.36-.52-1.32-1.26-1.67-1.26-1.67-1.03-.7.08-.69.08-.69 1.14.08 1.74 1.17 1.74 1.17 1.01 1.73 2.65 1.23 3.3.94.1-.73.4-1.23.72-1.51-2.53-.29-5.19-1.27-5.19-5.63 0-1.24.44-2.26 1.17-3.05-.12-.29-.51-1.45.11-3.02 0 0 .96-.31 3.15 1.16a10.9 10.9 0 0 1 5.73 0c2.19-1.47 3.15-1.16 3.15-1.16.62 1.57.23 2.73.11 3.02.73.79 1.17 1.81 1.17 3.05 0 4.37-2.67 5.33-5.21 5.61.41.36.78 1.06.78 2.14v3.17c0 .3.21.66.79.55A10.53 10.53 0 0 0 23.5 12.02C23.5 5.74 18.27.5 12 .5z"/></svg>
      </a>
      <a href="https://linkedin.com/in/sreemaheshkumar-s-509798326" target="_blank" rel="noopener" aria-label="LinkedIn">
        <svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor"><path d="M20.45 20.45h-3.56v-5.57c0-1.33-.02-3.04-1.85-3.04-1.86 0-2.15 1.45-2.15 2.94v5.67H9.34V9h3.41v1.56h.05c.48-.9 1.64-1.85 3.38-1.85 3.6 0 4.27 2.37 4.27 5.46v6.28zM5.34 7.43a2.07 2.07 0 1 1 0-4.13 2.07 2.07 0 0 1 0 4.13zM7.12 20.45H3.56V9h3.56v11.45z"/></svg>
      </a>
      <a href="mailto:mahesh123qr@gmail.com" aria-label="Email">
        <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="2" y="4" width="20" height="16" rx="2"/><path d="m22 6-10 7L2 6"/></svg>
      </a>
    </div>
  </div>
  <div class="ide-card reveal-right tilt" style="transition-delay:.15s">
    <div class="ide-bar">
      <span class="ide-dot" style="background:#ff5f57"></span>
      <span class="ide-dot" style="background:#febc2e"></span>
      <span class="ide-dot" style="background:#28c840"></span>
      <div class="ide-tab-row"><span class="ide-tab">Developer.java</span></div>
    </div>
    <div class="ide-body" id="typedCode"></div>
    <div class="terminal-box" id="terminalBox">
      <div id="terminalLog"></div>
      <div class="t-row">
        <span class="t-prompt">&rarr;</span>&nbsp;<span class="t-cwd">~</span>
        <span id="termTypedHint"></span>
        <input type="text" id="terminalInput" class="t-input" autocomplete="off" spellcheck="false" aria-label="Interactive terminal"/>
        <span class="t-cursor" aria-hidden="true"></span>
      </div>
    </div>
  </div>
</div>
</div>
</section>
<hr class="divider"/>

<section id="about">
<div class="container">
  <div class="s-label reveal">About me</div>
  <h2 class="s-title reveal" style="transition-delay:.08s">Who <span class="grad-text">I Am</span></h2>
  <div class="about-grid">
    <div class="about-photo-wrap reveal-left" tabindex="0" style="transition-delay:.1s">
      <img class="about-photo" src="assets/portfolio-mine-photo.png" alt="Portrait of Sreemaheshkumar S"/>
      <div class="about-photo-tint"></div>
      <div class="about-border"></div>
      <div class="about-photo-hint">hover to reveal &rarr;</div>
    </div>
    <div class="about-text reveal-right" style="transition-delay:.15s">
      <p>I'm a Computer Science fresher from <strong>Tirunelveli, Tamil Nadu</strong>, with hands-on full-stack expertise in Java, Spring Boot, and React.js. Over the past year I've moved from coursework into shipping two production-grade applications &mdash; each with real authentication, role-based access control, and relational data at the core.</p>
      <p>During my internship at <strong>Infosys Springboard</strong>, I engineered MedVault end-to-end: a multi-role healthcare platform with JWT-secured APIs, real-time slot management, and an OTP-secured payment flow. Alongside that, I built EcoWaste, a logistics platform connecting consumers with certified recyclers via the Google Maps API.</p>
      <p>I care about clean separation of concerns, normalized schemas, and code that's genuinely <strong>production-ready</strong> &mdash; not just demo-ready. Currently looking for a Software Developer role.</p>
      <div class="stat-row stagger">
        <div class="stat-card"><div class="stat-num grad-text">7.20</div><div class="stat-label">CGPA / 10</div></div>
        <div class="stat-card"><div class="stat-num grad-text">2</div><div class="stat-label">Apps Shipped</div></div>
        <div class="stat-card"><div class="stat-num grad-text">3+</div><div class="stat-label">Certifications</div></div>
        <div class="stat-card"><div class="stat-num grad-text">&infin;</div><div class="stat-label">Drive to Build</div></div>
      </div>
    </div>
  </div>
</div>
</section>
<hr class="divider"/>

<section id="skills">
<div class="container">
  <div class="s-label reveal">Technical stack</div>
  <h2 class="s-title reveal" style="transition-delay:.08s">My <span class="grad-text">Toolbox</span></h2>
  <p class="s-sub reveal" style="transition-delay:.14s">Languages, frameworks and tools I reach for when turning a spec into a working system.</p>
  <div class="skills-grid stagger">
    <div class="skill-card"><div class="skill-icon">&#9749;</div><div class="skill-cat">Languages</div><div class="skill-name">Java &amp; SQL</div><div class="skill-tags-row"><span class="skill-tag">Java</span><span class="skill-tag">SQL</span><span class="skill-tag">HTML5</span><span class="skill-tag">CSS3</span></div></div>
    <div class="skill-card"><div class="skill-icon">&#9883;</div><div class="skill-cat">Frontend</div><div class="skill-name">React Ecosystem</div><div class="skill-tags-row"><span class="skill-tag">React.js</span><span class="skill-tag">Bootstrap</span><span class="skill-tag">TailwindCSS</span><span class="skill-tag">Responsive</span></div></div>
    <div class="skill-card"><div class="skill-icon">&#127807;</div><div class="skill-cat">Backend</div><div class="skill-name">Spring Boot</div><div class="skill-tags-row"><span class="skill-tag">Spring Boot</span><span class="skill-tag">Node.js</span><span class="skill-tag">REST APIs</span><span class="skill-tag">JWT &middot; RBAC</span></div></div>
    <div class="skill-card"><div class="skill-icon">&#128024;</div><div class="skill-cat">Database</div><div class="skill-name">MySQL</div><div class="skill-tags-row"><span class="skill-tag">MySQL</span><span class="skill-tag">SQL Server</span><span class="skill-tag">Schema Design</span></div></div>
    <div class="skill-card"><div class="skill-icon">&#128296;</div><div class="skill-cat">Dev Tools</div><div class="skill-name">Git &amp; IDEs</div><div class="skill-tags-row"><span class="skill-tag">Git</span><span class="skill-tag">GitHub</span><span class="skill-tag">IntelliJ IDEA</span><span class="skill-tag">VS Code</span></div></div>
    <div class="skill-card"><div class="skill-icon">&#129513;</div><div class="skill-cat">Concepts</div><div class="skill-name">Engineering</div><div class="skill-tags-row"><span class="skill-tag">OOP</span><span class="skill-tag">Agile / SDLC</span><span class="skill-tag">DSA</span><span class="skill-tag">MVC</span></div></div>
  </div>
</div>
</section>
<hr class="divider"/>

<section id="experience">
<div class="container">
  <div class="s-label reveal">Work History</div>
  <h2 class="s-title reveal" style="transition-delay:.08s">Work <span class="grad-text">Experience</span></h2>
  <div class="timeline" style="max-width:780px">
    <div class="timeline-item reveal" style="transition-delay:.1s">
      <div class="exp-card glass">
        <div class="exp-top">
          <span class="exp-role">Java Full Stack Developer Intern</span>
          <span class="exp-date">Oct 2025 &mdash; Dec 2025</span>
        </div>
        <div class="exp-company">Infosys Springboard</div>
        <ul class="exp-list">
          <li>Engineered <strong>MedVault</strong> &mdash; a production-grade healthcare platform using Java, Spring Boot, React.js, and MySQL following MVC architecture, delivering end-to-end appointment and records management.</li>
          <li>Secured all API endpoints with JWT-based authentication and Role-Based Access Control (RBAC) across Patient, Doctor, and Admin roles, eliminating unauthorized access.</li>
          <li>Reduced scheduling conflicts by implementing real-time slot management with concurrency handling, OTP-secured UPI payment flow, and access-controlled medical records.</li>
        </ul>
      </div>
    </div>
  </div>
</div>
</section>
<hr class="divider"/>

<section id="projects">
<div class="container">
  <div class="s-label reveal">Selected Work</div>
  <h2 class="s-title reveal" style="transition-delay:.08s">Featured <span class="grad-text">Projects</span></h2>
  <p class="s-sub reveal" style="transition-delay:.14s">Two full-stack systems built from database schema to deployed UI &mdash; not tutorials, real multi-role platforms.</p>
  <div class="projects-grid">
    <div class="project-card reveal tilt" style="transition-delay:.1s">
      <div class="project-visual">
        <svg width="0" height="0"><defs><linearGradient id="rg" x1="0%" y1="0%" x2="100%" y2="0%"><stop offset="0%" stop-color="#7c3aed"/><stop offset="100%" stop-color="#2563eb"/></linearGradient></defs></svg>
        <div>
          <div class="cal-grid">
            <div class="cal-row"><div class="cal-cell"><div class="cal-fill"></div></div><div class="cal-cell"><div class="cal-fill"></div></div><div class="cal-cell"><div class="cal-fill"></div></div><div class="cal-cell"><div class="cal-fill"></div></div></div>
            <div class="cal-row"><div class="cal-cell"><div class="cal-fill"></div></div><div class="cal-cell"><div class="cal-fill"></div></div><div class="cal-cell"><div class="cal-fill"></div></div><div class="cal-cell"><div class="cal-fill"></div></div></div>
          </div>
          <div class="cal-cap">slot.<b>lock()</b> &rarr; zero conflicts</div>
        </div>
        <span class="p-stat">0 double-bookings</span>
      </div>
      <div class="project-body">
        <div class="project-num">01 / Healthcare Platform</div>
        <h3 class="project-name">MedVault</h3>
        <p class="project-desc">Appointment booking &amp; medical records system with 3 user roles, real-time slot conflict detection, and OTP-secured UPI payments.</p>
        <div class="project-tags"><span class="project-tag">Java</span><span class="project-tag">Spring Boot</span><span class="project-tag">React.js</span><span class="project-tag">MySQL</span><span class="project-tag">JWT</span><span class="project-tag">RBAC</span></div>
        <div class="project-links">
          <a class="p-link" href="https://github.com/Imahez/MedVault" target="_blank" rel="noopener">
            <svg width="15" height="15" viewBox="0 0 24 24" fill="currentColor"><path d="M12 .5C5.73.5.5 5.74.5 12.02c0 5.02 3.26 9.28 7.78 10.79.57.1.78-.25.78-.55v-2.14c-3.17.69-3.83-1.36-3.83-1.36-.52-1.32-1.26-1.67-1.26-1.67-1.03-.7.08-.69.08-.69 1.14.08 1.74 1.17 1.74 1.17 1.01 1.73 2.65 1.23 3.3.94.1-.73.4-1.23.72-1.51-2.53-.29-5.19-1.27-5.19-5.63 0-1.24.44-2.26 1.17-3.05-.12-.29-.51-1.45.11-3.02 0 0 .96-.31 3.15 1.16a10.9 10.9 0 0 1 5.73 0c2.19-1.47 3.15-1.16 3.15-1.16.62 1.57.23 2.73.11 3.02.73.79 1.17 1.81 1.17 3.05 0 4.37-2.67 5.33-5.21 5.61.41.36.78 1.06.78 2.14v3.17c0 .3.21.66.79.55A10.53 10.53 0 0 0 23.5 12.02C23.5 5.74 18.27.5 12 .5z"/></svg>
            Source Code
          </a>
          <button class="p-link primary" onclick="openModal('medvault')">Case Study &rarr;</button>
        </div>
      </div>
    </div>
    <div class="project-card reveal tilt" style="transition-delay:.18s">
      <div class="project-visual">
        <div>
          <div class="route-wrap">
            <svg viewBox="0 0 160 80">
              <defs><linearGradient id="rg2" x1="0%" y1="0%" x2="100%" y2="0%"><stop offset="0%" stop-color="#7c3aed"/><stop offset="100%" stop-color="#22d3ee"/></linearGradient></defs>
              <path class="route-path" d="M16,58 C 50,12 110,12 144,58"/>
              <circle cx="16" cy="58" r="5" class="route-pin"/>
              <circle cx="144" cy="58" r="5" class="route-pin"/>
              <circle r="4" class="route-pin"><animateMotion dur="3.4s" repeatCount="indefinite" rotate="auto" path="M16,58 C 50,12 110,12 144,58"/></circle>
            </svg>
            <div class="route-cap">gps.<b>route()</b> &rarr; pickup en route</div>
          </div>
        </div>
        <span class="p-stat">&minus;60% manual follow-up</span>
      </div>
      <div class="project-body">
        <div class="project-num">02 / Logistics Platform</div>
        <h3 class="project-name">EcoWaste</h3>
        <p class="project-desc">Smart e-waste collection platform connecting consumers with certified recyclers via Maps-based pickup scheduling and real-time routing.</p>
        <div class="project-tags"><span class="project-tag">Java</span><span class="project-tag">Spring Boot</span><span class="project-tag">React.js</span><span class="project-tag">MySQL</span><span class="project-tag">Google Maps API</span></div>
        <div class="project-links">
          <a class="p-link" href="https://github.com/Imahez/EcoWaste" target="_blank" rel="noopener">
            <svg width="15" height="15" viewBox="0 0 24 24" fill="currentColor"><path d="M12 .5C5.73.5.5 5.74.5 12.02c0 5.02 3.26 9.28 7.78 10.79.57.1.78-.25.78-.55v-2.14c-3.17.69-3.83-1.36-3.83-1.36-.52-1.32-1.26-1.67-1.26-1.67-1.03-.7.08-.69.08-.69 1.14.08 1.74 1.17 1.74 1.17 1.01 1.73 2.65 1.23 3.3.94.1-.73.4-1.23.72-1.51-2.53-.29-5.19-1.27-5.19-5.63 0-1.24.44-2.26 1.17-3.05-.12-.29-.51-1.45.11-3.02 0 0 .96-.31 3.15 1.16a10.9 10.9 0 0 1 5.73 0c2.19-1.47 3.15-1.16 3.15-1.16.62 1.57.23 2.73.11 3.02.73.79 1.17 1.81 1.17 3.05 0 4.37-2.67 5.33-5.21 5.61.41.36.78 1.06.78 2.14v3.17c0 .3.21.66.79.55A10.53 10.53 0 0 0 23.5 12.02C23.5 5.74 18.27.5 12 .5z"/></svg>
            Source Code
          </a>
          <button class="p-link primary" onclick="openModal('ecowaste')">Case Study &rarr;</button>
        </div>
      </div>
    </div>
  </div>
</div>
</section>

<div class="modal-overlay" id="modalOverlay"><div class="modal-box" id="modalContent"></div></div>
<hr class="divider"/>

<section id="certifications">
<div class="container">
  <div class="s-label reveal">Credentials</div>
  <h2 class="s-title reveal" style="transition-delay:.08s">Certs &amp; <span class="grad-text">Education</span></h2>
  <div class="split-grid">
    <div class="cert-list stagger">
      <div class="cert-card"><div class="cert-ico"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 4h16v16H4z"/><path d="m8 12 3 3 5-6"/></svg></div><div><h4>Programming Using Java</h4><span>NPTEL</span></div></div>
      <div class="cert-card"><div class="cert-ico"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 4h16v16H4z"/><path d="m8 12 3 3 5-6"/></svg></div><div><h4>Data Structures &amp; Algorithms Using Java</h4><span>Infosys Springboard</span></div></div>
      <div class="cert-card"><div class="cert-ico"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 4h16v16H4z"/><path d="m8 12 3 3 5-6"/></svg></div><div><h4>Database Management Systems</h4><span>Infosys Springboard</span></div></div>
    </div>
    <div class="edu-card glass reveal-right" style="transition-delay:.1s">
      <h4>B.E. &mdash; Computer Science &amp; Engineering</h4>
      <div class="edu-inst">Cape Institute of Technology, Tirunelveli</div>
      <div class="edu-row"><span>Duration</span><b>Jul 2022 &ndash; May 2026</b></div>
      <div class="edu-row"><span>CGPA</span><b>7.20 / 10</b></div>
      <div class="edu-row"><span>Location</span><b>Tirunelveli, Tamil Nadu</b></div>
    </div>
  </div>
</div>
</section>
<hr class="divider"/>

<section id="contact">
<div class="container">
  <div class="s-label reveal">Say hello</div>
  <h2 class="s-title reveal" style="transition-delay:.08s">Let's <span class="grad-text">Build Together</span></h2>
  <p class="s-sub reveal" style="transition-delay:.14s">Open to Software Developer roles and full-stack opportunities. Reach out or send a message below.</p>
  <div class="contact-grid">
    <div class="contact-info reveal-left" style="transition-delay:.1s">
      <div class="contact-item" title="Click to copy"><div class="contact-ico"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="2" y="4" width="20" height="16" rx="2"/><path d="m22 6-10 7L2 6"/></svg></div><div><h4>Email</h4><p>mahesh123qr@gmail.com</p></div></div>
      <div class="contact-item" title="Click to copy"><div class="contact-ico"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07A19.5 19.5 0 0 1 4.19 12 19.79 19.79 0 0 1 1.12 3.38 2 2 0 0 1 3.11 1.1h3a2 2 0 0 1 2 1.72c.127.96.361 1.903.7 2.81a2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45c.907.339 1.85.573 2.81.7A2 2 0 0 1 22 16.92z"/></svg></div><div><h4>Phone</h4><p>+91 86800 72366</p></div></div>
      <a class="contact-item" href="https://linkedin.com/in/sreemaheshkumar-s-509798326" target="_blank" rel="noopener"><div class="contact-ico"><svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor"><path d="M20.45 20.45h-3.56v-5.57c0-1.33-.02-3.04-1.85-3.04-1.86 0-2.15 1.45-2.15 2.94v5.67H9.34V9h3.41v1.56h.05c.48-.9 1.64-1.85 3.38-1.85 3.6 0 4.27 2.37 4.27 5.46v6.28zM5.34 7.43a2.07 2.07 0 1 1 0-4.13 2.07 2.07 0 0 1 0 4.13zM7.12 20.45H3.56V9h3.56v11.45z"/></svg></div><div><h4>LinkedIn</h4><p>sreemaheshkumar-s</p></div></a>
      <a class="contact-item" href="https://github.com/Imahez" target="_blank" rel="noopener"><div class="contact-ico"><svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor"><path d="M12 .5C5.73.5.5 5.74.5 12.02c0 5.02 3.26 9.28 7.78 10.79.57.1.78-.25.78-.55v-2.14c-3.17.69-3.83-1.36-3.83-1.36-.52-1.32-1.26-1.67-1.26-1.67-1.03-.7.08-.69.08-.69 1.14.08 1.74 1.17 1.74 1.17 1.01 1.73 2.65 1.23 3.3.94.1-.73.4-1.23.72-1.51-2.53-.29-5.19-1.27-5.19-5.63 0-1.24.44-2.26 1.17-3.05-.12-.29-.51-1.45.11-3.02 0 0 .96-.31 3.15 1.16a10.9 10.9 0 0 1 5.73 0c2.19-1.47 3.15-1.16 3.15-1.16.62 1.57.23 2.73.11 3.02.73.79 1.17 1.81 1.17 3.05 0 4.37-2.67 5.33-5.21 5.61.41.36.78 1.06.78 2.14v3.17c0 .3.21.66.79.55A10.53 10.53 0 0 0 23.5 12.02C23.5 5.74 18.27.5 12 .5z"/></svg></div><div><h4>GitHub</h4><p>github.com/Imahez</p></div></a>
    </div>
    <form class="form-card glass reveal-right" id="contactForm" style="transition-delay:.12s">
      <div class="form-row"><label for="fname">Name</label><input type="text" id="fname" name="name" placeholder="Your name" required/></div>
      <div class="form-row"><label for="femail">Email</label><input type="email" id="femail" name="email" placeholder="you@example.com" required/></div>
      <div class="form-row"><label for="fmsg">Message</label><textarea id="fmsg" name="message" placeholder="Tell me about the role or project..." required></textarea></div>
      <button type="submit" class="submit-btn" id="submitBtn">Send Message &rarr;</button>
      <div class="form-msg" id="formMsg"></div>
    </form>
  </div>
</div>
</section>

<footer>
<div class="container">
  <div class="footer-inner">
    <p class="footer-copy">&copy; <span id="yr"></span> Sreemaheshkumar S &mdash; built with care in pure HTML, CSS &amp; JS &middot; <a href="https://github.com/Imahez" target="_blank" rel="noopener">GitHub</a></p>
    <a href="#home" class="back-top" aria-label="Back to top">
      <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="m18 15-6-6-6 6"/></svg>
    </a>
  </div>
</div>
</footer>
"""

JS = """
'use strict';
const pfm  = window.matchMedia('(prefers-reduced-motion:reduce)').matches;
const fine = window.matchMedia('(hover:hover) and (pointer:fine)').matches;
const mob  = window.innerWidth < 768;
const $  = (s,c=document) => c.querySelector(s);

// Year
if($('#yr')) $('#yr').textContent = new Date().getFullYear();

// Nav scroll
const header = $('#site-header');
const secs   = document.querySelectorAll('section[id]');
const navAs  = document.querySelectorAll('.nav-links a');
function onScroll(){
  header.classList.toggle('scrolled', window.scrollY > 24);
  let cur='';
  secs.forEach(s=>{if(window.scrollY>=s.offsetTop-140)cur=s.id});
  navAs.forEach(a=>a.classList.toggle('active',a.getAttribute('href')==='#'+cur));
  const pct=(window.scrollY/(document.documentElement.scrollHeight-window.innerHeight)*100).toFixed(1);
  const sp=$('#scroll-progress');if(sp)sp.style.width=pct+'%';
}
window.addEventListener('scroll',onScroll,{passive:true});

// Burger
const burger=$('#burgerBtn'),mNav=$('#mobileNav');
if(burger&&mNav){burger.addEventListener('click',()=>mNav.classList.toggle('open'));mNav.querySelectorAll('a').forEach(a=>a.addEventListener('click',()=>mNav.classList.remove('open')));}

// Reveal
const rio=new IntersectionObserver(es=>{es.forEach(e=>{if(e.isIntersecting){e.target.classList.add('in');rio.unobserve(e.target);}});},{threshold:.1,rootMargin:'0px 0px -50px 0px'});
document.querySelectorAll('.reveal,.reveal-left,.reveal-right,.reveal-scale,.stagger').forEach(el=>rio.observe(el));

// Canvas particles
(function(){
  if(pfm)return;
  const cv=$('#bg-canvas'),ctx=cv.getContext('2d');
  let W,H;
  function rsz(){W=cv.width=window.innerWidth;H=cv.height=window.innerHeight;}rsz();
  let rt;window.addEventListener('resize',()=>{clearTimeout(rt);rt=setTimeout(rsz,120);});
  const N=mob?30:70;
  class P{
    constructor(init){
      this.x=Math.random()*(W||800);
      this.y=init?Math.random()*(H||600):(H||600)+10;
      this.r=Math.random()*2+.3;this.vx=(Math.random()-.5)*.3;this.vy=-(Math.random()*.5+.15);
      this.a=0;this.maxA=Math.random()*.5+.1;this.spd=Math.random()*.005+.002;this.fading=false;
      const pals=[['rgba(124,58,237,','rgba(79,70,229,','rgba(167,139,250,'],['rgba(37,99,235,','rgba(96,165,250,','rgba(34,211,238,'],['rgba(255,255,255,']];
      const p=pals[Math.floor(Math.random()*pals.length)];this.color=p[Math.floor(Math.random()*p.length)];
      this.gr=this.r*(Math.random()*5+4);
    }
    update(){this.x+=this.vx;this.y+=this.vy;if(!this.fading&&this.a<this.maxA)this.a+=this.spd;if(this.y<(H||600)*.1)this.fading=true;if(this.fading)this.a-=this.spd*1.6;if(this.a<=0&&this.fading)Object.assign(this,new P(false));}
    draw(){const g=ctx.createRadialGradient(this.x,this.y,0,this.x,this.y,this.gr);g.addColorStop(0,this.color+(this.a*.85).toFixed(3)+')');g.addColorStop(1,this.color+'0)');ctx.beginPath();ctx.arc(this.x,this.y,this.gr,0,Math.PI*2);ctx.fillStyle=g;ctx.fill();ctx.beginPath();ctx.arc(this.x,this.y,this.r,0,Math.PI*2);ctx.fillStyle=this.color+Math.min(this.a*2,1).toFixed(3)+')';ctx.fill();}
  }
  const ps=Array.from({length:N},(_,i)=>new P(i<N));
  function tick(){ctx.clearRect(0,0,W,H);ps.forEach(p=>{p.update();p.draw();});requestAnimationFrame(tick);}
  requestAnimationFrame(tick);
})();

// Stars
(function(){
  if(pfm)return;
  const hero=$('#home');if(!hero)return;
  const N=mob?25:50;
  for(let i=0;i<N;i++){const s=document.createElement('span');s.className='star';const sz=Math.random()*2.2+.4;s.style.cssText=`width:${sz}px;height:${sz}px;left:${Math.random()*100}%;top:${Math.random()*100}%;--dur:${(2.5+Math.random()*4).toFixed(2)}s;--delay:${(Math.random()*5).toFixed(2)}s;--max:${(.2+Math.random()*.5).toFixed(2)};`;hero.appendChild(s);}
})();

// Parallax + spotlight
(function(){
  if(pfm||mob)return;
  let tx=0,ty=0,cx=0,cy=0;
  const blobs=document.querySelectorAll('.aurora-blob'),grid=$('.bg-grid'),LERP=.055,D=[.018,.028,.012,.022];
  window.addEventListener('mousemove',e=>{tx=(e.clientX/innerWidth-.5)*2;ty=(e.clientY/innerHeight-.5)*2;document.documentElement.style.setProperty('--sx',e.clientX);document.documentElement.style.setProperty('--sy',e.clientY);},{passive:true});
  function loop(){cx+=(tx-cx)*LERP;cy+=(ty-cy)*LERP;document.documentElement.style.setProperty('--mx',cx.toFixed(4));document.documentElement.style.setProperty('--my',cy.toFixed(4));blobs.forEach((b,i)=>{const dx=cx*D[i]*innerWidth,dy=cy*D[i]*innerHeight;b.style.transform=`translate(${dx.toFixed(1)}px,${dy.toFixed(1)}px)`;});requestAnimationFrame(loop);}
  loop();
})();

// Cursor
(function(){
  if(!fine||pfm)return;
  const dot=$('#cursor-dot'),ring=$('#cursor-ring');if(!dot||!ring)return;
  document.body.classList.add('cursor-active');
  let mx=innerWidth/2,my=innerHeight/2,rx=mx,ry=my,magX=null,magY=null,isMag=false,activeEl=null;
  const LN=.09,LM=.17;
  const SC={home:'#7c3aed',about:'#60a5fa',skills:'#a78bfa',experience:'#38bdf8',projects:'#7c3aed',certifications:'#34d399',contact:'#7c3aed'};
  let cc='#7c3aed';
  function ac(c){if(c===cc)return;cc=c;document.documentElement.style.setProperty('--cursor-color',c);dot.style.boxShadow=`0 0 8px 3px ${c},0 0 20px 6px ${c}55`;}
  const cio2=new IntersectionObserver(es=>{es.forEach(e=>{if(e.isIntersecting)ac(SC[e.target.id]||'#7c3aed');});},{threshold:.4});
  document.querySelectorAll('section[id]').forEach(s=>cio2.observe(s));
  const MS='button,.btn,.nav-resume,.submit-btn,.p-link,.back-top,.nav-burger',EX='a,.skill-card,.project-card,.cert-card,.stat-card,.contact-item',TX='p,li,.about-text p,.exp-list li';
  function setState(st){ring.classList.remove('expanded','magnetic','text-mode');dot.style.opacity='1';if(st==='magnetic'){ring.classList.add('magnetic');dot.style.opacity='.4';}else if(st==='expanded')ring.classList.add('expanded');else if(st==='text')ring.classList.add('text-mode');}
  window.addEventListener('mousemove',e=>{mx=e.clientX;my=e.clientY;if(isMag&&activeEl){const r=activeEl.getBoundingClientRect(),ecx=r.left+r.width/2,ecy=r.top+r.height/2;magX=ecx+(e.clientX-ecx)*.35;magY=ecy+(e.clientY-ecy)*.35;activeEl.style.transform=`translate(${((e.clientX-ecx)*.12).toFixed(2)}px,${((e.clientY-ecy)*.12).toFixed(2)}px)`;}else{magX=null;magY=null;}},{passive:true});
  document.addEventListener('mouseover',e=>{const t=e.target;if(t.closest(MS)){activeEl=t.closest(MS);isMag=true;setState('magnetic');}else if(t.closest(EX)){activeEl=t.closest(EX);isMag=false;setState('expanded');}else if(t.closest(TX)){activeEl=null;isMag=false;setState('text');}});
  document.addEventListener('mouseout',e=>{if(e.target.closest(MS)){const t=e.target.closest(MS);t.style.transform='';t.style.transition='transform .4s cubic-bezier(.25,.46,.45,.94)';setTimeout(()=>{t.style.transition='';},420);}if(!e.relatedTarget||(!e.relatedTarget.closest(MS)&&!e.relatedTarget.closest(EX)&&!e.relatedTarget.closest(TX))){isMag=false;activeEl=null;magX=null;magY=null;setState('default');}});
  document.addEventListener('mousedown',()=>dot.classList.add('clicking'));
  document.addEventListener('mouseup',()=>dot.classList.remove('clicking'));
  document.addEventListener('mouseleave',()=>{dot.classList.add('hidden');ring.classList.add('hidden');});
  document.addEventListener('mouseenter',()=>{dot.classList.remove('hidden');ring.classList.remove('hidden');});
  let tf=0;window.addEventListener('mousemove',e=>{tf++;if(tf%2)return;const td=document.createElement('div');td.className='trail-dot';td.style.left=e.clientX+'px';td.style.top=e.clientY+'px';const s=.3+Math.random()*.7;td.style.transform=`translate(-50%,-50%) scale(${s})`;document.body.appendChild(td);setTimeout(()=>td.remove(),580);},{passive:true});
  function loop(){dot.style.transform=`translate(${mx}px,${my}px) translate(-50%,-50%)`;const ttx=(isMag&&magX!==null)?magX:mx,tty=(isMag&&magY!==null)?magY:my,l=isMag?LM:LN;rx+=(ttx-rx)*l;ry+=(tty-ry)*l;ring.style.transform=`translate(${rx.toFixed(2)}px,${ry.toFixed(2)}px) translate(-50%,-50%)`;requestAnimationFrame(loop);}
  loop();
})();

// Tilt
(function(){
  if(!fine||pfm||mob)return;
  document.querySelectorAll('.tilt').forEach(card=>{
    card.addEventListener('mousemove',e=>{const r=card.getBoundingClientRect(),dx=(e.clientX-r.left-r.width/2)/(r.width/2),dy=(e.clientY-r.top-r.height/2)/(r.height/2);card.style.transform=`perspective(1200px) rotateX(${(-dy*7).toFixed(2)}deg) rotateY(${(dx*7).toFixed(2)}deg) scale(1.015)`;card.style.setProperty('--tx',((e.clientX-r.left)/r.width*100).toFixed(1)+'%');card.style.setProperty('--ty',((e.clientY-r.top)/r.height*100).toFixed(1)+'%');});
    card.addEventListener('mouseleave',()=>{card.style.transform='perspective(1200px) rotateX(0) rotateY(0) scale(1)';card.style.transition='transform .5s cubic-bezier(.25,.46,.45,.94)';setTimeout(()=>{card.style.transition='';},520);});
  });
})();

// Timeline
(function(){
  const tl=$('.timeline');if(!tl)return;
  function upd(){const r=tl.getBoundingClientRect();const p=Math.max(0,Math.min(1,(innerHeight*.8-r.top)/r.height));tl.style.setProperty('--tl',p.toFixed(3));}
  window.addEventListener('scroll',upd,{passive:true});upd();
})();

// Decode animation
(function(){
  const CH='!<>-_\\\\/[]{}=+*^?#________';
  function dec(el,delay){const fin=el.dataset.final||'',finH=el.dataset.html||'';if(pfm){el.innerHTML=finH||fin;return;}let it=0,fr=0;setTimeout(()=>{const id=setInterval(()=>{fr++;el.textContent=fin.split('').map((c,i)=>{if(i<it)return fin[i];return i%2===0?CH[Math.floor(Math.random()*CH.length)]:c;}).join('');if(fr%3===0)it++;if(it>=fin.length){clearInterval(id);el.innerHTML=finH||fin;}},35);},delay);}
  document.querySelectorAll('.decode-line').forEach((el,i)=>dec(el,i*340));
})();

// Typing IDE
(function(){
  const el=$('#typedCode');if(!el)return;
  const cH=`<span class="ln">1</span><span class="kw">public class</span> <span class="cls">Developer</span> {\n<span class="ln">2</span>  <span class="kw">private</span> String name = <span class="str">"Sreemaheshkumar S"</span>;\n<span class="ln">3</span>  <span class="kw">private</span> String role = <span class="str">"Java Full Stack Dev"</span>;\n<span class="ln">4</span>  <span class="kw">private</span> String[] stack = {<span class="str">"Java"</span>,<span class="str">"Spring"</span>,<span class="str">"React"</span>};\n<span class="ln">5</span>  <span class="cmt">// Shipped: MedVault, EcoWaste</span>\n<span class="ln">6</span>  <span class="kw">public</span> <span class="fn">boolean</span> <span class="fn">isHireable</span>() {\n<span class="ln">7</span>    <span class="kw">return</span> <span class="fn">true</span>;\n<span class="ln">8</span>  }\n<span class="ln">9</span>}`;
  const pT=`1 public class Developer {\n2   private String name = "Sreemaheshkumar S";\n3   private String role = "Java Full Stack Dev";\n4   private String[] stack = {"Java","Spring","React"};\n5   // Shipped: MedVault, EcoWaste\n6   public boolean isHireable() {\n7     return true;\n8   }\n9 }`;
  function type(){if(pfm){el.innerHTML=cH;return;}let i=0;el.textContent='';const id=setInterval(()=>{el.textContent=pT.slice(0,i)+'|';i+=2;if(i>pT.length){clearInterval(id);el.innerHTML=cH;typeHint();}},14);}
  function typeHint(){const h=$('#termTypedHint');const msg='type help -> ';if(!h||pfm)return;let j=0;const id=setInterval(()=>{h.textContent=msg.slice(0,j++);if(j>msg.length){clearInterval(id);h.style.opacity='1';setTimeout(()=>{h.style.opacity='0';h.textContent='';},3000);}},60);}
  if(document.readyState==='loading')document.addEventListener('DOMContentLoaded',type);else type();
})();

// Terminal
(function(){
  const log=$('#terminalLog'),inp=$('#terminalInput');if(!log||!inp)return;
  const CMD={help:()=>[['dim','available commands:'],['dim','  about | skills | experience | projects | contact'],['dim','  whoami | sudo hire-me | ls | clear']],whoami:()=>[['out','fresher who ships production code, not tutorials.']],about:()=>[['out','navigating to about.md...']],skills:()=>[['out','loading skills.json...']],experience:()=>[['out','opening experience.log...']],projects:()=>[['out','listing projects/...']],contact:()=>[['out','opening contact.sh...']],ls:()=>[['out','about.md  skills.json  experience.log  projects/  contact.sh']],'sudo hire-me':()=>[['hl','Permission granted. Redirecting to contact.sh...']]};
  const NAV={about:'#about',skills:'#skills',experience:'#experience',projects:'#projects',contact:'#contact','sudo hire-me':'#contact'};
  function print(lines){lines.forEach(([cls,txt])=>{const d=document.createElement('div');d.className='line '+cls;d.textContent=txt;log.appendChild(d);});log.scrollTop=log.scrollHeight;}
  inp.addEventListener('keydown',e=>{if(e.key!=='Enter')return;const cmd=inp.value.trim().toLowerCase();inp.value='';if(!cmd)return;const ec=document.createElement('div');ec.className='line echo';ec.textContent=cmd;log.appendChild(ec);if(cmd==='clear'){log.innerHTML='';return;}const h=CMD[cmd];if(h){const r=h();print(r);if(NAV[cmd])setTimeout(()=>document.querySelector(NAV[cmd])?.scrollIntoView({behavior:'smooth'}),400);}else{print([['dim',`command not found: ${cmd}. try 'help'`]]);}log.scrollTop=log.scrollHeight;});
  const tb=$('#terminalBox');if(tb)tb.addEventListener('click',()=>inp.focus());
})();

// Modals
const PROJECTS={medvault:{title:'MedVault - Healthcare Booking and Records Platform',tags:['Java','Spring Boot','React.js','TailwindCSS','MySQL','JWT','RBAC'],points:['Architected a scalable multi-role healthcare platform supporting Patient, Doctor, and Admin roles with appointment scheduling, payment processing, and medical records access control.','Engineered real-time slot conflict detection and OTP-secured UPI payment integration, achieving zero double-booking incidents in testing.','Delivered clean MVC separation: React.js + TailwindCSS frontend, Spring Boot REST backend, normalized MySQL schema - production-ready and fully documented.'],link:'https://github.com/Imahez/MedVault'},ecowaste:{title:'EcoWaste - Smart E-Waste Collection Platform',tags:['Java','Spring Boot','React.js','MySQL','Google Maps API'],points:['Built a full-stack e-waste management platform connecting consumers with certified recyclers, supporting Admin, Pickup Personnel, and Customer roles with granular workflow controls.','Integrated Google Maps API for location-based pickup scheduling with real-time geographic routing and distance calculation.','Automated email notification pipeline for real-time status updates across the pickup lifecycle, reducing manual follow-up by an estimated 60%.'],link:'https://github.com/Imahez/EcoWaste'}};
const ov=$('#modalOverlay'),mc=$('#modalContent');
window.openModal=function(key){const d=PROJECTS[key];mc.innerHTML=`<button class="modal-close" onclick="closeModal()">x</button><h3>${d.title}</h3><div class="modal-tags">${d.tags.map(t=>`<span class="project-tag">${t}</span>`).join('')}</div><ul>${d.points.map(p=>`<li>${p}</li>`).join('')}</ul><a href="${d.link}" target="_blank" rel="noopener" class="btn btn-primary" style="margin-top:18px;display:inline-flex;">View on GitHub</a>`;ov.classList.add('open');};
window.closeModal=function(){ov.classList.remove('open');};
if(ov)ov.addEventListener('click',e=>{if(e.target===ov)closeModal();});
document.addEventListener('keydown',e=>{if(e.key==='Escape')closeModal();});

// Contact
const form=$('#contactForm'),sb=$('#submitBtn'),fm=$('#formMsg');
if(form){form.addEventListener('submit',function(e){e.preventDefault();sb.disabled=true;sb.textContent='Sending...';fm.className='form-msg';fm.textContent='';emailjs.send('service_h0veyvj','template_b35cc5a',{from_name:$('#fname').value.trim(),from_email:$('#femail').value.trim(),message:$('#fmsg').value.trim(),to_name:'Mahesh'}).then(()=>{fm.textContent='Message sent - I will reply soon!';fm.classList.add('ok');form.reset();}).catch(err=>{console.error(err);fm.textContent='Failed - please email mahesh123qr@gmail.com directly.';fm.classList.add('err');}).finally(()=>{sb.disabled=false;sb.textContent='Send Message';});});}

// Copy to clipboard
document.querySelectorAll('.contact-item[title="Click to copy"]').forEach(item=>{item.addEventListener('click',()=>{const p=item.querySelector('p');if(!p)return;navigator.clipboard?.writeText(p.textContent.trim()).then(()=>{const o=p.textContent;p.textContent='Copied!';setTimeout(()=>{p.textContent=o;},1800);});});});

onScroll();
"""

# Replace CSS placeholder in HTML
html_out = HTML.replace("CSS_PLACEHOLDER", CSS)

# Wrap JS in script tags
final = html_out.replace("</footer>", "</footer>\n<script>\n" + JS + "\n</script>\n</body>\n</html>")

# Remove the placeholder </body></html> from HTML since we added them above
# Actually HTML template doesn't have them - let's just write as is with the script appended
# Final content
output = html_out + "\n<script>\n" + JS + "\n</script>\n</body>\n</html>"

with open("index.html", "w", encoding="utf-8") as f:
    f.write(output)

size = os.path.getsize("index.html")
print(f"SUCCESS: index.html written, size={size} bytes")
