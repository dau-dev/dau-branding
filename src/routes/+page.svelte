<script lang="ts">
  import { BrandMark, Button, CookieNotice, SpecTable, Split, ThemeToggle } from '#lib';

  const palette = [
    { token: '--dau-bg', lit: '#eeede9', shadow: '#202021', role: 'Page background' },
    { token: '--dau-bg-raised', lit: '#e4e3de', shadow: '#28282a', role: 'Raised surfaces, hover' },
    { token: '--dau-border', lit: '#cfcdc7', shadow: '#3a3a3c', role: 'Rules and outlines' },
    { token: '--dau-fg-muted', lit: '#5d5c58', shadow: '#9b9a96', role: 'Supporting text, labels' },
    { token: '--dau-fg', lit: '#202021', shadow: '#eeede9', role: 'Text, the filled half of the disk, focus' }
  ];

  const scale = [
    { name: 'Display', spec: '300 / 4.5rem / -0.04em', sample: 'Data, accelerated.', size: '4.5rem', weight: 300 },
    {
      name: 'Heading',
      spec: '600 / 2rem / -0.02em',
      sample: 'Measured on physical hardware.',
      size: '2rem',
      weight: 600
    },
    {
      name: 'Body',
      spec: '400 / 1.0625rem / 1.6',
      sample: 'Unsupported operations run on the CPU, and the fallback is visible.',
      size: '1.0625rem',
      weight: 400
    }
  ];
</script>

<svelte:head><title>dau brand kit</title></svelte:head>

<main>
  <header>
    <BrandMark />
    <ThemeToggle />
  </header>

  <section class="intro">
    <h1>dau brand kit</h1>
    <p class="lede">
      Tokens, marks, and Svelte components for dau.dev and anything else that carries the dau name. The rules behind
      them are in <code>BRAND.md</code>.
    </p>
  </section>

  <section aria-labelledby="mark">
    <h2 id="mark">Mark</h2>
    <p>
      A half-filled disk inside a chip package. The line across the disk is the split between hardware and what stays in
      software. Below 32px drop the package and use the disk alone.
    </p>
    <div class="marks">
      <div class="tile dau-shadow"><BrandMark href={null} size={56} /></div>
      <div class="tile dau-lit"><BrandMark href={null} size={56} /></div>
      <div class="tile dau-shadow"><BrandMark href={null} size={56} wordmark={false} /></div>
      <div class="tile dau-lit row">
        <BrandMark href={null} variant="disk" size={24} />
        <BrandMark href={null} variant="disk" size={16} wordmark={false} />
      </div>
    </div>
  </section>

  <section aria-labelledby="color">
    <h2 id="color">Color</h2>
    <p>Two colors and the steps between them. There is no accent; emphasis comes from flipping a surface.</p>
    <SpecTable
      headings={['Token', 'Lit / shadow', 'Role']}
      rows={palette.map((p) => ({ key: p.token, value: `${p.lit} / ${p.shadow}`, note: p.role }))}
    />
    <div class="swatches" aria-hidden="true">
      {#each palette as p (p.token)}
        <div class="sw">
          <i style:background={p.lit}></i>
          <i style:background={p.shadow}></i>
        </div>
      {/each}
    </div>
  </section>

  <section aria-labelledby="type">
    <h2 id="type">Type</h2>
    <p>Hanken Grotesk for text, Fragment Mono for labels, tables, and code. Both are self-hosted.</p>
    <div class="scale">
      {#each scale as s (s.name)}
        <div class="step">
          <span class="meta">{s.name} · {s.spec}</span>
          <span style:font-size={s.size} style:font-weight={s.weight} class="sample">{s.sample}</span>
        </div>
      {/each}
      <div class="step">
        <span class="meta">Mono · 400 / 0.8125rem</span>
        <code class="sample">LOAD_PHASE @ 0x0084</code>
      </div>
    </div>
  </section>

  <section aria-labelledby="components">
    <h2 id="components">Components</h2>
    <h3>Button</h3>
    <div class="row">
      <Button href="#components">Become a design partner</Button>
      <Button href="#components" variant="secondary">See the code</Button>
      <Button size="sm">Got it</Button>
    </div>

    <h3>Split</h3>
    <Split>
      {#snippet hardware()}
        <p class="split-h strong">Scans run on the FPGA.</p>
        <p class="split-p">Filters, derived columns, and aggregations stream through tiles built for the workload.</p>
      {/snippet}
      {#snippet software()}
        <p class="split-h">Everything else runs in Polars.</p>
        <p class="split-p">If the loaded configuration doesn't cover an operation, it runs on the CPU.</p>
      {/snippet}
    </Split>

    <h3>SpecTable</h3>
    <SpecTable
      caption="dpv2"
      rows={[
        { key: 'Logic', value: '204K LUTs' },
        { key: 'Memory', value: '2 GB onboard + 8 GB SODIMM DDR3' },
        { key: 'Host link', value: 'PCIe x8' }
      ]}
    />

    <h3>CookieNotice</h3>
    <p>Fixed to the bottom of the viewport until dismissed; this page shows a live one.</p>
  </section>
</main>

<CookieNotice>dau.dev sets no cookies and runs no analytics. <a href="#components">Privacy</a></CookieNotice>

<style>
  main {
    width: min(calc(100% - 2rem), 64rem);
    margin: 0 auto;
    padding: 2rem 0 10rem;
  }

  header {
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 1.5rem;
    padding-bottom: 1.5rem;
    border-bottom: 1px solid var(--dau-border);
  }

  h1 {
    margin: 0 0 0.75rem;
    font-size: clamp(2.25rem, 6vw, 3.5rem);
    font-weight: 300;
    letter-spacing: -0.04em;
  }

  h2 {
    margin: 0 0 0.5rem;
    font-size: 1.5rem;
    font-weight: 600;
    letter-spacing: -0.02em;
  }

  h3 {
    margin: 2rem 0 0.75rem;
    color: var(--dau-fg-muted);
    font-family: var(--dau-font-mono);
    font-size: 0.75rem;
    font-weight: 400;
    letter-spacing: 0.08em;
    text-transform: uppercase;
  }

  section {
    margin-top: 3.5rem;
  }

  section > p,
  .lede {
    max-width: 62ch;
    margin: 0 0 1.5rem;
    color: var(--dau-fg-muted);
    line-height: 1.6;
  }

  code {
    font-family: var(--dau-font-mono);
  }

  .marks {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(13rem, 1fr));
    gap: 1px;
    border: 1px solid var(--dau-border);
    background: var(--dau-border);
  }

  .tile {
    display: grid;
    min-height: 9rem;
    place-items: center;
  }

  .row {
    display: flex;
    flex-wrap: wrap;
    align-items: center;
    gap: 1rem;
  }

  .tile.row {
    justify-content: center;
  }

  .swatches {
    display: grid;
    grid-template-columns: repeat(5, minmax(0, 1fr));
    margin-top: 1.5rem;
    border: 1px solid var(--dau-border);
  }

  .sw i {
    display: block;
    height: 3rem;
  }

  .scale {
    display: grid;
    gap: 1.5rem;
  }

  .step {
    display: grid;
    gap: 0.35rem;
    padding-bottom: 1.5rem;
    border-bottom: 1px solid var(--dau-border);
  }

  .meta {
    color: var(--dau-fg-muted);
    font-family: var(--dau-font-mono);
    font-size: 0.75rem;
  }

  .sample {
    line-height: 1.1;
    letter-spacing: -0.02em;
    overflow-wrap: anywhere;
  }

  .split-h {
    margin: 0;
    font-size: clamp(1.5rem, 3.5vw, 2.25rem);
    font-weight: 300;
    letter-spacing: -0.03em;
    line-height: 1.05;
  }

  .split-h.strong {
    font-weight: 700;
  }

  .split-p {
    max-width: 34ch;
    margin: 0.85rem 0 0;
    color: var(--dau-fg-muted);
  }
</style>
