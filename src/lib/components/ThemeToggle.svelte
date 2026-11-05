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
  {theme === 'dark' ? 'Light' : 'Dark'}
</button>

<style>
  button {
    padding: 0.5rem 0.75rem;
    border: 1px solid var(--dau-border);
    color: var(--dau-fg);
    background: var(--dau-bg);
    cursor: pointer;
  }
</style>
