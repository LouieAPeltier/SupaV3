<script lang="ts">
  import ListCard from '../lib/components/ListCard.svelte';

  const sampleLists = [
    {
      title: 'Best Street Foods',
      description: 'Tacos, ramen, satay, and all the iconic street snacks.',
      score: 12
    },
    {
      title: 'Top Productivity Habits',
      description: 'Morning planning, deep work blocks, and daily review.',
      score: 8
    }
  ];
</script>

<main>
  <header>
    <p class="badge">ListRank beta setup</p>
    <h1>Ranked lists that everyone can vote on</h1>
    <p>
      Public-first lists, Firebase auth/storage ready, and built to iterate quickly.
    </p>
    <button>Create a list</button>
  </header>

  <section>
    {#each sampleLists as list}
      <ListCard {...list} />
    {/each}
  </section>
</main>

<style>
  main {
    max-width: 920px;
    margin: 0 auto;
    padding: 2rem 1rem 4rem;
    display: grid;
    gap: 1.5rem;
  }

  header {
    background: linear-gradient(130deg, #ff6a00, #ff9348);
    color: white;
    padding: 2rem;
    border-radius: 1.25rem;
  }

  h1 {
    margin: 0.4rem 0;
  }

  .badge {
    display: inline-block;
    padding: 0.3rem 0.7rem;
    background: rgba(255, 255, 255, 0.2);
    border-radius: 999px;
    margin: 0;
  }

  section {
    display: grid;
    gap: 1rem;
  }
</style>
