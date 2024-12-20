var brojacSlika = 1;
window.onload = function() {
    fetch('/viz/obrisiSlike');
    brojacSlika = 1;
};
window.addEventListener('unload', function() {
    fetch('/viz/obrisiSlike');
    brojacSlika = 1;
});
document.getElementById('parametriForm').addEventListener('submit', function (e) {
    e.preventDefault();
    if(document.getElementById('rezultati'))
        document.getElementById('rezultati').remove();
    fetch('/viz/obrisiSlike');
    brojacSlika = 1;
    fetch('/viz/betweennessCentralityPodaci')
        .then(response => response.json())
        .then(data => {
            const rezultatiDiv = document.createElement('div');
            rezultatiDiv.id = 'rezultati';
            rezultatiDiv.innerHTML = '';
            if (data.brSlika > 0) {
                const slika = document.getElementById("trSlikaAlg");
                if(slika)
                    slika.remove();
                const img = document.createElement('img');
                img.id = 'trSlikaAlg';
                img.src = '../slike/slika1.png?' + new Date().getTime();
                img.style.width = '850px';
                rezultatiDiv.appendChild(img);
                document.body.appendChild(rezultatiDiv);
            } else
                rezultatiDiv.innerHTML = '<p>Nema rezultata za prikaz.</p>';
    })
    .catch(err => console.error('Greška:', err));
});