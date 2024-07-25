document.addEventListener("DOMContentLoaded", () => {
    const detailsContainer = document.getElementById('pokemon-details');
    const selectedPokemon = JSON.parse(localStorage.getItem('selectedPokemon'));
    console.log(selectedPokemon);
        const detailsDiv = document.createElement('div');
        detailsDiv.classList.add('pokemon-details');
        detailsDiv.innerHTML = `
            <h2>${selectedPokemon.name}</h2>
            <img src="${selectedPokemon.sprites.front_default}" alt="${selectedPokemon.name}">
            <p>Height: ${selectedPokemon.height}</p>
            <p>Weight: ${selectedPokemon.weight}</p>
            <p>Type: ${selectedPokemon.types.map(typeInfo => typeInfo.type.name).join(', ')}</p>
            <p>Abilities: ${selectedPokemon.abilities.map(abilityInfo => abilityInfo.ability.name).join(', ')}</p>
        `;
        detailsContainer.appendChild(detailsDiv);
});
