<script lang="ts">
  import { onMount, type Snippet } from 'svelte';
  import Button from './Button.svelte';

  interface Props {
    /** localStorage key remembering the dismissal. */
    storageKey?: string;
    /** Notice text. Say what the site actually stores. */
    children: Snippet;
  }

  let { storageKey = 'dau.cookie-notice', children }: Props = $props();
  let visible = $state(false);

  onMount(() => {
    try {
      visible = localStorage.getItem(storageKey) !== 'dismissed';
    } catch {
      visible = true;
    }
  });

  function dismiss() {
    visible = false;
    try {
      localStorage.setItem(storageKey, 'dismissed');
    } catch {
      // Storage unavailable: hide for this page view only.
    }
  }
</script>

{#if visible}
  <div class="notice dau-shadow" role="region" aria-label="Cookie notice" data-testid="cookie-notice">
    <div class="inner">
      <p>{@render children()}</p>
      <Button size="sm" onclick={dismiss} data-testid="cookie-notice-dismiss">Got it</Button>
    </div>
  </div>
{/if}

<style>
  .notice {
    position: fixed;
    inset: auto 0 0;
    z-index: 60;
    padding: 0.875rem max(1rem, env(safe-area-inset-right, 0px)) calc(0.875rem + env(safe-area-inset-bottom, 0px))
      max(1rem, env(safe-area-inset-left, 0px));
    border-top: 1px solid var(--dau-border);
  }

  .inner {
    display: flex;
    flex-wrap: wrap;
    align-items: center;
    gap: 0.75rem 1.5rem;
    max-width: 72rem;
    margin: 0 auto;
  }

  p {
    flex: 1 1 20rem;
    min-width: 0;
    margin: 0;
    color: var(--dau-fg-muted);
    font-size: 0.875rem;
    line-height: 1.5;
  }

  p :global(a) {
    color: var(--dau-fg);
    text-decoration: underline;
  }
</style>
