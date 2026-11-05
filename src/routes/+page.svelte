<script lang="ts">
  import { BrandMark, ThemeToggle } from '#lib';
</script>

<svelte:head><title>dau brand kit</title></svelte:head>

<main>
  <header>
    <BrandMark />
    <ThemeToggle />
  </header>

  <h1>dau</h1>
  <p class="lede">dau brand identity, design tokens, theme system, and reusable Svelte components.</p>

  <section aria-labelledby="tokens">
    <h2 id="tokens">Tokens</h2>
    <p>
      Colors, type, and spacing live in <code>src/lib/styles/tokens.css</code>. The values there are neutral
      placeholders — replace them with the brand's own.
    </p>
  </section>
</main>

<style>
  main {
    width: min(calc(100% - 3rem), 64rem);
    margin: 0 auto;
    padding: 3rem 0 6rem;
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
    margin: 2.5rem 0 0.5rem;
    font-size: 1.75rem;
    font-weight: 600;
  }

  h2 {
    margin: 0 0 0.5rem;
    font-size: 1rem;
    font-weight: 600;
  }

  .lede {
    margin: 0;
    max-width: 60ch;
    color: var(--dau-fg-muted);
  }

  section {
    margin-top: 2.5rem;
    max-width: 60ch;
  }

  section p {
    margin: 0;
    color: var(--dau-fg-muted);
  }

  code {
    font-family: var(--dau-font-mono);
  }
</style>
