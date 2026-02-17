<script lang="ts">
  export let title: string;
  export let description: string;
  export let score = 0;
</script>

<article class="card">
  <div>
    <h3>{title}</h3>
    <p>{description}</p>
  </div>
  <div class="score">🔥 {score}</div>
  <button>Vote +1</button>
</article>

<style>
  .card {
    display: grid;
    gap: 0.75rem;
    background: white;
    border: 2px solid #ffd8bf;
    border-radius: 1rem;
    padding: 1rem;
  }

  h3 {
    margin: 0;
    color: #c84f00;
  }

  p {
    margin: 0.3rem 0 0;
  }

  .score {
    font-weight: 700;
  }
</style>
