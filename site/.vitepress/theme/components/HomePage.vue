<script setup>
import { withBase } from 'vitepress'

const base = withBase
</script>

<template>
  <section class="home-hero">
    <div class="home-hero__panel home-hero__copy">
      <span class="home-kicker">Open Standard</span>
      <h1 class="home-title">One professional identity.<br>Unlimited representations.</h1>
      <p class="home-subtitle">
        ResumeSpec is an open standard for representing professional identity as structured,
        portable, machine-readable data. It defines the model, semantics, JSON Schema contract,
        examples, and a reference implementation without tying identity to any single visual format
        or vendor workflow.
      </p>

      <div class="home-actions">
        <a class="home-button home-button--primary" :href="base('/specification/')">Read the Specification</a>
        <a class="home-button home-button--secondary" :href="base('/get-started/quick-start')">Get Started</a>
        <a class="home-button home-button--secondary" href="https://github.com/4k4m1m3-org/ResumeSpec">View on GitHub</a>
      </div>

      <div class="home-stats" aria-label="ResumeSpec highlights">
        <div class="home-stat">
          <strong>Open Standard</strong>
          <span>Public spec, public schema, public examples.</span>
        </div>
        <div class="home-stat">
          <strong>Machine-readable</strong>
          <span>JSON Schema Draft 2020-12 as executable contract.</span>
        </div>
        <div class="home-stat">
          <strong>Portable</strong>
          <span>Structured data that can travel across tools and platforms.</span>
        </div>
        <div class="home-stat">
          <strong>Developer-first</strong>
          <span>Clear docs, reference Python implementation, reproducible tests.</span>
        </div>
      </div>
    </div>

    <aside class="home-hero__panel hero-visual">
      <img class="hero-banner" :src="base('/banner.png')" alt="ResumeSpec banner" />
      <div class="hero-meta">
        <div class="hero-meta__label">Current release</div>
        <h2 class="hero-meta__title">ResumeSpec v1.0.0</h2>
        <p style="margin: 0; color: var(--vp-c-text-2); line-height: 1.65">
          The first stable release is published and tagged. The canonical format is JSON;
          YAML and XML remain supported by the reference implementation as secondary formats.
        </p>
        <div class="hero-meta__links">
          <a class="chip" href="https://github.com/4k4m1m3-org/ResumeSpec/releases/tag/v1.0.0">v1.0.0 Release</a>
          <a class="chip" :href="base('/reference/python')">Python Reference</a>
          <a class="chip" :href="base('/examples/json')">Examples</a>
        </div>
      </div>
    </aside>
  </section>

  <section class="section-shell">
    <h2 class="section-title">Why ResumeSpec?</h2>
    <p class="section-lead">
      Professional information is usually fragmented across CVs, portfolios, LinkedIn, ATS platforms,
      job systems, databases, and proprietary APIs. ResumeSpec starts from a different assumption:
      one structured identity should be able to produce many representations without losing meaning.
    </p>

    <div class="feature-grid" style="margin-top: 1rem">
      <div class="mini-card">
        <h3>CVs</h3>
        <p>Document layouts optimized for hiring workflows and human review.</p>
      </div>
      <div class="mini-card">
        <h3>LinkedIn</h3>
        <p>Platform profiles that reflect the same career facts in a different surface.</p>
      </div>
      <div class="mini-card">
        <h3>Portfolios</h3>
        <p>Curated public pages that emphasize projects, links, and evidence.</p>
      </div>
      <div class="mini-card">
        <h3>ATS / APIs / AI</h3>
        <p>Systems that consume structured, deterministic professional identity data.</p>
      </div>
    </div>
  </section>

  <section class="section-shell">
    <h2 class="section-title">One identity, many representations</h2>
    <p class="section-lead">
      ResumeSpec does not replace downstream formats. It gives them a common source of truth.
      The ecosystem can then render, validate, or consume the same identity in different ways.
    </p>

    <div class="diagram" style="margin-top: 1rem">
<pre>ResumeSpec
    │
    ▼
Structured professional identity
    │
    ├─ JSON
    ├─ YAML
    └─ XML
    │
    ▼
Validators / parsers / tools
    │
    ▼
Resumes / portfolios / ATS / APIs / AI</pre>
    </div>
  </section>

  <section class="section-shell">
    <h2 class="section-title">Built for machines and humans</h2>
    <div class="two-up" style="margin-top: 1rem">
      <div class="home-section mini-card">
        <h3>Structured data</h3>
        <p>ResumeSpec is defined as data, not presentation. The schema makes structure explicit and reproducible.</p>
      </div>
      <div class="home-section mini-card">
        <h3>JSON first</h3>
        <p>JSON is the canonical v1 format and the authoritative machine-readable contract is the JSON Schema.</p>
      </div>
      <div class="home-section mini-card">
        <h3>YAML supported</h3>
        <p>The Python reference implementation can parse YAML as a secondary format for convenience.</p>
      </div>
      <div class="home-section mini-card">
        <h3>XML supported</h3>
        <p>XML parsing is supported by the reference implementation and hardened with `defusedxml`.</p>
      </div>
    </div>
  </section>

  <section class="section-shell">
    <h2 class="section-title">Current v1.0.0</h2>
    <div class="status-grid" style="margin-top: 1rem">
      <div class="status-card status-card--now">
        <span class="roadmap-pill roadmap-pill--now">Available now</span>
        <h3>Specification, schema, examples, parser, validator, CLI</h3>
        <ul>
          <li>Stable v1.0.0 contract.</li>
          <li>Reference Python implementation.</li>
          <li>Executable examples and tests.</li>
          <li>Release tag: <a href="https://github.com/4k4m1m3-org/ResumeSpec/releases/tag/v1.0.0">v1.0.0</a>.</li>
        </ul>
      </div>
      <div class="status-card status-card--future">
        <span class="roadmap-pill roadmap-pill--future">Roadmap</span>
        <h3>Docs ecosystem, SDKs, generators, integrations</h3>
        <ul>
          <li>Documentation website expansion.</li>
          <li>Multi-language SDKs.</li>
          <li>PDF and portfolio generators.</li>
          <li>ATS exporters, scoring, AI, XSD, registry.</li>
        </ul>
      </div>
    </div>
  </section>

  <section class="section-shell">
    <h2 class="section-title">Open standard</h2>
    <p class="section-lead">
      ResumeSpec is open source, versioned, and contribution-friendly. The release is published on
      GitHub and the standard is designed to evolve without collapsing into a product-specific format.
    </p>

    <div class="link-grid" style="margin-top: 1rem">
      <a class="home-section mini-card docs-link" href="https://github.com/4k4m1m3-org/ResumeSpec">Repository</a>
      <a class="home-section mini-card docs-link" href="https://github.com/4k4m1m3-org/ResumeSpec/issues">Issues</a>
      <a class="home-section mini-card docs-link" href="https://github.com/4k4m1m3-org/ResumeSpec/discussions">Discussions</a>
      <a class="home-section mini-card docs-link" href="https://github.com/4k4m1m3-org/ResumeSpec/releases">Releases</a>
    </div>

    <div class="home-callout page-card" style="margin-top: 1rem">
      <h3 style="margin-top: 0">Help build the standard</h3>
      <p style="margin-bottom: 0">
        ResumeSpec is being built as an open standard. Contributions are welcome across the spec,
        examples, implementation, tests, and documentation.
      </p>
      <div class="home-actions" style="margin-top: 1rem">
        <a class="home-button home-button--primary" :href="base('/community/contributing')">Contribute to ResumeSpec</a>
        <a class="home-button home-button--secondary" :href="base('/community/roadmap')">See the roadmap</a>
      </div>
    </div>
  </section>
</template>
