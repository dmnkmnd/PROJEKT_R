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
    document.getElementById('rezultati').remove();
    fetch('/viz/obrisiSlike');
    brojacSlika = 1;
    const cvorA = document.getElementById('cvorA').value;
    const cvorB = document.getElementById('cvorB').value;
    fetch('/viz/AdamecAdarIndexPodaci?cvorA=' + cvorA + '&cvorB=' + cvorB)
        .then(response => response.json())
        .then(data => {
            const rezultatiDiv = document.createElement('div');
            rezultatiDiv.id = 'rezultati';
            rezultatiDiv.innerHTML = '';
            if (data.brSlika > 0) {
                const slika = document.getElementById("trSlikaAlg");
                if(slika)
                    slika.remove();
                const nazadBtn = document.createElement('button');
                nazadBtn.textContent = 'Nazad';
                nazadBtn.id = 'nazadBtn';
                nazadBtn.addEventListener('click', function () {
                    if(brojacSlika > 1) {
                        document.getElementById("trSlikaAlg").remove();
                        brojacSlika--;
                        const trSlika = document.createElement('img');
                        trSlika.id = 'trSlikaAlg';
                        trSlika.src = '../slike/slika' + brojacSlika + '.png?' + new Date().getTime();
                        trSlika.style.width = '850px';
                        rezultatiDiv.appendChild(trSlika);
                    }
                });
                rezultatiDiv.appendChild(nazadBtn);
                const naprijedBtn = document.createElement('button');
                naprijedBtn.textContent = 'Naprijed';
                naprijedBtn.id = 'naprijedBtn';
                naprijedBtn.addEventListener('click', function () {
                    if(brojacSlika < data.brSlika) {
                        document.getElementById("trSlikaAlg").remove();
                        brojacSlika++;
                        const trSlika = document.createElement('img');
                        trSlika.id = 'trSlikaAlg';
                        trSlika.src = '../slike/slika' + brojacSlika + '.png?' + new Date().getTime();
                        trSlika.style.width = '850px';
                        rezultatiDiv.appendChild(trSlika);
                    }
                });
                rezultatiDiv.appendChild(naprijedBtn);
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