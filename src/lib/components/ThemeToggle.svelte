<script lang="ts">
  import { onMount } from 'svelte';
  import { initTheme, toggleTheme, type ResolvedTheme } from '../theme.js';

  let theme = $state<ResolvedTheme>('light');
  onMount(() => {
    theme = initTheme();
  });
</script>

<button
  type="button"
  data-testid="theme-toggle"
  aria-label={`Switch to ${theme === 'dark' ? 'light' : 'dark'} mode`}
  onclick={() => (theme = toggleTheme())}
>
  <svg width="16" height="16" viewBox="0 0 16 16" aria-hidden="true">
    <circle cx="8" cy="8" r="6.5" fill="none" stroke="currentColor" stroke-width="1.5" />
    <path d={theme === 'dark' ? 'M8 1.5a6.5 6.5 0 0 0 0 13z' : 'M8 1.5a6.5 6.5 0 0 1 0 13z'} fill="currentColor" />
  </svg>
</button>

<style>
  button {
    display: inline-grid;
    width: 2.25rem;
    height: 2.25rem;
    place-items: center;
    padding: 0;
    border: 1px solid var(--dau-border);
    border-radius: var(--dau-radius);
    color: var(--dau-fg);
    background: transparent;
    cursor: pointer;
  }

  button:hover {
    background: var(--dau-bg-raised);
  }
</style>
