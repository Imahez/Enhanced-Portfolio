# Premium Portfolio React Components Setup

These reusable components bring high-performance, custom background and cursor interactions into any React + Vite portfolio.

## Folder Structure

Copy these files into your React project:

```
src/
├── components/
│   ├── CustomCursor/
│   │   ├── CustomCursor.jsx
│   │   └── CustomCursor.module.css
│   ├── InteractiveBackground/
│   │   ├── InteractiveBackground.jsx
│   │   └── InteractiveBackground.module.css
│   └── Magnetic/
│       └── Magnetic.jsx
├── hooks/
│   └── usePrefersReducedMotion.js
```

## Integration Guide

Import the components at the top level of your application (usually inside `src/App.jsx`):

```jsx
import React from 'react';
import InteractiveBackground from './components/InteractiveBackground/InteractiveBackground';
import CustomCursor from './components/CustomCursor/CustomCursor';
import Magnetic from './components/Magnetic/Magnetic';

function App() {
  return (
    <>
      {/* 1. Global Interactivity Systems */}
      <InteractiveBackground />
      <CustomCursor />

      {/* 2. Page Content */}
      <main style={{ position: 'relative', z-index: 1 }}>
        <header>
          <h1>Mahesh Dev</h1>
        </header>

        {/* 3. Magnetic Component Wrapper */}
        <section>
          <Magnetic strength={0.4} range={60}>
            <button className="cta-btn">
              Get In Touch
            </button>
          </Magnetic>
        </section>
      </main>
    </>
  );
}

export default App;
```

---

# Fixing vercel 404: NOT_FOUND (Pure Static Deployments)

If you are deploying a **pure static HTML portfolio** (non-React) and receive a `404: NOT_FOUND` error, follow these steps to configure Vercel correctly.

### Why does this error occur?
Vercel automatically detects project structures. If Vercel mistakenly detects a framework preset (such as Vite or React) in your project settings, it will look for a build output folder (like `dist` or `build`). Since a pure HTML project does not have a build command, the folder is empty or not found, causing Vercel to serve a 404 error page.

### The Fix

1. **Framework Preset:** In the Vercel project dashboard, go to **Settings** -> **General** and verify that the **Framework Preset** is set to **"Other"** (or static hosting) instead of Vite/React.
2. **`vercel.json` Setup:** Make sure your `vercel.json` file in the root directory matches this clean configuration (which has been updated in your codebase):
```json
{
  "cleanUrls": true
}
```
This configuration removes custom `outputDirectory` declarations that can override the static folder serving root, ensuring that your `index.html` at the root is served directly.
