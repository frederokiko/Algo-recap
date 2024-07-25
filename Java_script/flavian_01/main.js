document.addEventListener("DOMContentLoaded", () => {
    const container = document.getElementById('pokemon');

    const fetchPokemon = async () => {     
            const response = await fetch('https://pokeapi.co/api/v2/pokemon?limit=50');
            const data = await response.json();
            displayPokemon(data.results);
            console.log(data.results);
    };

    const displayPokemon = (pokemonList) => {
        pokemonList.forEach(async (pokemon) => { 
                const response = await fetch(pokemon.url);
                const data = await response.json();
                const pokemonDiv = document.createElement('div');
                pokemonDiv.classList.add('pokemon');
                pokemonDiv.innerHTML = `
                    <h2>Nom :</h2>
                    <h2>${data.name}</h2>
                    <p>Clique moi 👁‍🗨</p>
                    <img src="${data.sprites.front_default}" alt="${data.name}">
                `;
                pokemonDiv.addEventListener('click', () => {
                    localStorage.setItem('selectedPokemon', JSON.stringify(data));
                    window.location.href = 'mapage2.html';
                });
                container.appendChild(pokemonDiv);
        });
    };

    fetchPokemon();
});

