document.getElementById('valide').addEventListener('click', () => {
    const text = document.getElementById('texte').value;

    const comptemot = text.trim().split(/\s+/).filter(word => word.length > 0).length;

    const arobase = text.includes('@');

    const longueur = text.length;

    const aprecu = text.slice(0, 100);


    document.getElementById('comptemot').textContent = comptemot;
    document.getElementById('aroba').textContent = arobase ? '@ trouvé' : '@ non trouvé';
    document.getElementById('long').textContent = longueur;
    document.getElementById('apercu').textContent = aprecu;
});