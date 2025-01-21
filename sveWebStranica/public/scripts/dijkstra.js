var brojacSlika = 1;
window.onload = function() {
    document.getElementById('nazadBtn').style.display = 'inline';
    document.getElementById('naprijedBtn').style.display = 'inline';
    document.getElementById('rezultati').style.display = 'none';
    fetch('/viz/obrisiSlike');
    brojacSlika = 1;
};
window.addEventListener('unload', function() {
    document.getElementById('nazadBtn').style.display = 'inline';
    document.getElementById('naprijedBtn').style.display = 'inline';
    document.getElementById('rezultati').style.display = 'none';
    fetch('/viz/obrisiSlike');
    brojacSlika = 1;
});
document.getElementById('parametriForm').addEventListener('submit', function (e) {
    e.preventDefault();
    document.getElementById('nazadBtn').style.display = 'inline';
    document.getElementById('naprijedBtn').style.display = 'inline';
    document.getElementById('rezultati').style.display = 'none';
    fetch('/viz/obrisiSlike');
    brojacSlika = 1;
    const cvorA = document.getElementById('cvorA').value;
    const cvorB = document.getElementById('cvorB').value;
    const preskakanje = document.getElementById('preskakanje').value;
    fetch('/viz/dijkstrinAlgoritamPodaci?cvorA=' + cvorA + '&cvorB=' + cvorB + '&preskakanje=' + preskakanje)
        .then(response => response.json())
        .then(data => {
            if (data.brSlika > 0) {
                const slika = document.getElementById("trSlikaAlg");
                if(slika)
                    slika.remove();

                const nazadBtn = document.getElementById('nazadBtn');
                const naprijedBtn = document.getElementById('naprijedBtn');

                const nazadClickHandler = function () {
                    document.getElementById('naprijedBtn').style.display = 'inline';
                    if(brojacSlika > 1) {
                        document.getElementById("trSlikaAlg").remove();
                        brojacSlika--;
                        const trSlika = document.createElement('img');
                        trSlika.id = 'trSlikaAlg';
                        trSlika.src = '../slike/slika' + brojacSlika + '.png?' + new Date().getTime();
                        trSlika.style.width = '100%';
                        document.getElementById("rezultatiSlika").appendChild(trSlika);
                    }
                    if(brojacSlika == 1)
                        document.getElementById('nazadBtn').style.display = 'none';
                };

                const naprijedClickHandler = function () {
                    document.getElementById('nazadBtn').style.display = 'inline';
                    if(brojacSlika < data.brSlika) {
                        document.getElementById("trSlikaAlg").remove();
                        brojacSlika++;
                        const trSlika = document.createElement('img');
                        trSlika.id = 'trSlikaAlg';
                        trSlika.src = '../slike/slika' + brojacSlika + '.png?' + new Date().getTime();
                        trSlika.style.width = '100%';
                        document.getElementById("rezultatiSlika").appendChild(trSlika);
                    }
                    if(brojacSlika == data.brSlika)
                        document.getElementById('naprijedBtn').style.display = 'none';
                };

                nazadBtn.replaceWith(nazadBtn.cloneNode(true));
                naprijedBtn.replaceWith(naprijedBtn.cloneNode(true));

                document.getElementById('nazadBtn').addEventListener('click', nazadClickHandler);
                document.getElementById('naprijedBtn').addEventListener('click', naprijedClickHandler);

                const img = document.createElement('img');
                img.id = 'trSlikaAlg';
                img.src = '../slike/slika1.png?' + new Date().getTime();
                img.style.width = '100%';
                document.getElementById("rezultatiSlika").appendChild(img);
                document.getElementById('nazadBtn').style.display = 'none';
                document.getElementById('rezultati').style.display = 'flex';

                if(data.rez != -1) {
                    document.getElementById("porukaUdaljenost").style.color = 'black';
                    document.getElementById("porukaUdaljenost").innerText = 'minimalna udaljenost od čvora ' + cvorA + ' do čvora ' + cvorB + ' je ' + data.rez;
                }
                else {
                    document.getElementById("porukaUdaljenost").style.color = 'red';
                    document.getElementById("porukaUdaljenost").innerText = 'iz čvora ' + cvorA + ' nije moguće posjetiti čvor ' + cvorB + ' (udaljenost: ∞)';
                }
            }
    })
    .catch(err => console.error('Greška:', err));
});