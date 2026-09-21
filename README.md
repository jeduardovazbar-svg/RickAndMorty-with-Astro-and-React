<div align="center">

# 🧪 Dimension C-137: Rick & Morty Explorer
### Blazing-Fast Multiverse Directory Powered by Astro & React

[![Astro](https://img.shields.io/badge/Astro-5.0+-BC52EE?style=for-the-badge&logo=astro&logoColor=white)](https://astro.build)
[![React](https://img.shields.io/badge/React-19-61DAFB?style=for-the-badge&logo=react&logoColor=black)](https://react.dev)
[![TailwindCSS](https://img.shields.io/badge/Tailwind_CSS-38B2AC?style=for-the-badge&logo=tailwind-css&logoColor=white)](https://tailwindcss.com)
[![Rick & Morty API](https://img.shields.io/badge/API-Rick_&_Morty-97ce4c?style=for-the-badge&logo=graphql&logoColor=black)](https://rickandmortyapi.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](https://opensource.org/licenses/MIT)

<br />

<p align="center">
  <b>A hyper-optimized, interactive web application exploring the eccentric inhabitants of the Rick and Morty multiverse.</b>
  <br />
  Leveraging <i>Astro’s Island Architecture</i> for near-zero runtime overhead combined with rich, interactive <i>React</i> components.
</p>

[Explore Features](#-key-features) • [Preview & Screenshots](#-interface-preview) • [Tech Stack](#-architecture--tech-stack) • [Quickstart](#-getting-started)

---

</div>

## 🌌 Overview

**Dimension C-137: Rick & Morty Explorer** delivers instantaneous character indexing, deep filtering, and immersive visual profiles across infinite dimensions. 

By utilizing **Astro** as the static-first meta-framework and **React** for isolated dynamic UI elements, this project demonstrates how to eliminate JavaScript bloat while maintaining a dynamic single-page app experience.

---

## ✨ Key Features

- ⚡ **Island Architecture:** Critical UI shells and data layouts are pre-rendered at build time; dynamic interactive controls hydrate only on demand (`client:load` / `client:visible`).
- 🔍 **Real-Time Character Search:** Instantly search across names, species, origin, and alive/dead/unknown statuses.
- 🧬 **Interactive Character Dossiers:** Dedicated modal and deep-link views exposing origin locations, last known dimensions, and episode appearances.
- 🎨 **Cosmic Cyberpunk UI:** Custom glassmorphism, glowing accents, and smooth micro-animations tailored to the show's aesthetic.
- 📱 **Mobile-First Responsive Layout:** Adaptive grids transitioning seamlessly from compact mobile cards to ultra-wide displays.

---

## 📸 Interface Preview

### 1. Main Multiverse Catalog (Overview)
*Browse, filter, and paginate through hundreds of characters with zero initial layout shifts.*

<div align="center">
  <br />
  <!-- REPLACE THE URL BELOW WITH YOUR OVERVIEW SCREENSHOT -->
  <img src="https://images.unsplash.com/photo-1579546929518-9e396f3cc809?auto=format&fit=crop&w=1200&q=80" alt="Main Multiverse Overview Grid" width="90%" style="border-radius: 12px; border: 1px solid rgba(255, 255, 255, 0.1); box-shadow: 0 20px 40px -15px rgba(151, 206, 76, 0.25);" />
  <p><sub><b>Figure 1:</b> The character directory grid displaying live status badges and pagination controls.</sub></p>
  <br />
</div>

---

### 2. Character Dossier (Detailed View)
*In-depth breakdown of character origins, affiliations, and episodic chronologies.*

<div align="center">
  <br />
  <!-- REPLACE THE URL BELOW WITH YOUR CHARACTER DETAIL SCREENSHOT -->
  <img src="https://images.unsplash.com/photo-1618005182384-a83a8bd57fbe?auto=format&fit=crop&w=1200&q=80" alt="Character Detail Profile View" width="90%" style="border-radius: 12px; border: 1px solid rgba(255, 255, 255, 0.1); box-shadow: 0 20px 40px -15px rgba(97, 218, 251, 0.25);" />
  <p><sub><b>Figure 2:</b> Detailed profile inspect panel showing character lore, origin planet, and episode history.</sub></p>
  <br />
</div>

---

## 🛠 Architecture & Tech Stack

| Layer | Technology | Purpose |
| :--- | :--- | :--- |
| **Framework** | [Astro](https://astro.build/) | Static site generation (SSG), routing, and island hydration |
| **UI Components** | [React](https://react.dev/) | Interactive search bars, filter chips, and character modals |
| **Styling** | [Tailwind CSS](https://tailwindcss.com/) | Utility-first responsive design, dark mode, and neon color palettes |
| **API Provider** | [The Rick and Morty API](https://rickandmortyapi.com/) | REST endpoints for characters, locations, and episodes |
| **Icons** | [Lucide Icons](https://lucide.dev/) | Clean, lightweight UI iconography |

### How the Astro-React Island Integration Works:

```astro
---
// src/pages/characters/[id].astro
import MainLayout from '../../layouts/MainLayout.astro';
import CharacterProfileCard from '../../components/CharacterProfileCard.jsx';

export async function getStaticPaths() {
  const res = await fetch('https://rickandmortyapi.com/api/character');
  const data = await res.json();
  return data.results.map((char) => ({
    params: { id: char.id.toString() },
    props: { character: char },
  }));
}

const { character } = Astro.props;
---

<MainLayout title={`Profile | ${character.name}`}>
  <main class="container mx-auto px-4 py-8">
    <!-- React Component hydrated only on client view -->
    <CharacterProfileCard client:visible character={character} />
  </main>
</MainLayout>
```

---

## 🚀 Getting Started

Follow these steps to run the portal locally on your machine:

### Prerequisites
- **Node.js**: `v18.17.0` or higher
- **Package Manager**: `npm`, `pnpm`, or `bun`

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/rick-and-morty-astro-react.git
   cd rick-and-morty-astro-react
   ```

2. **Install dependencies:**
   ```bash
   npm install
   ```

3. **Launch the development server:**
   ```bash
   npm run dev
   ```

4. **Access the portal:**
   Open your browser and navigate to `http://localhost:4321`.

### Production Build

To test the production build with full static generation:

```bash
npm run build
npm run preview
```

---

## 📡 API Reference

This application communicates with the public **Rick and Morty REST API**:

- `GET /api/character` - Fetch paginated character index.
- `GET /api/character/{id}` - Fetch single character details.
- `GET /api/character/?name={query}&status={status}` - Dynamic query filters.

*Special thanks to [Axel Fuhrmann](https://github.com/afuh) for maintaining the free public API.*

---

## 📄 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.
