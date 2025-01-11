window.onload = function() {
    document.getElementById('rezultati').style.display = 'none';
    fetch('/viz/obrisiSlike');
};
window.addEventListener('unload', function() {
    document.getElementById('rezultati').style.display = 'none';
    fetch('/viz/obrisiSlike');
});
document.getElementById('parametriForm').addEventListener('submit', function (e) {
    e.preventDefault();
    document.getElementById('rezultati').style.display = 'none';
    fetch('/viz/obrisiSlike');
    const cvorA = document.getElementById('cvorA').value;
    const cvorB = document.getElementById('cvorB').value;
    fetch('/viz/AdamecAdarIndexPodaci?cvorA=' + cvorA + '&cvorB=' + cvorB)
        .then(response => response.json())
        .then(data => {
            if (data.brSlika > 0) {
                const slika = document.getElementById("trSlikaAlg");
                if(slika)
                    slika.remove();
                const img = document.createElement('img');
                img.id = 'trSlikaAlg';
                img.src = '../slike/slika1.png?' + new Date().getTime();
                img.style.width = '100%';
                document.getElementById("rezultatiSlika").appendChild(img);
                document.getElementById('rezultati').style.display = 'flex';
            }
    })
    .catch(err => console.error('Greška:', err));
});