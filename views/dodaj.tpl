% rebase ('base.tpl', title = 'Igra')
% import model

<h1>
    Dodajanje nalog
</h1>

<p>Vnesi del izbrane pesmi. 20 do 40 besed!</p>
<form action="/dodaj_pesem/" method="post">
    <div class="input-group">
        <div class="input-group-prepend">
            <span class="input-group-text">Izvajalec in naslov pesmi</span>
        </div>
        <input type="text" name="avtor" class="form-control">
        <input type="text" name="naslov" class="form-control">
    </div>
    <div class="input-group input-group-lg">
        <div class="input-group-prepend">
            <span class="input-group-text" id="inputGroup-sizing-lg">Besedilo</span>
        </div>
        <input type="text" class="form-control" name="besedilo" aria-describedby="inputGroup-sizing-lg">
    </div>
    <button type="submit">Vnesi podatke</button>
</form>

