% rebase ('base.tpl', title = 'Igra')
% import model

<h1>
    Dodajanje nalog
</h1>

<div class="alert alert-info" role="alert">
    Dodajate lahko po ena nalogo hkrati. Kjer morate vnesti dva podatka, vnesite vsakega v svoje okno.
</div>

<h3>Pesem</h3>
<p>Vnesi del izbrane pesmi. 20 do 50 besed!</p>
<form action="/dodaj_pesem/" method="post">
    <div class="input-group">
        <div class="input-group-prepend">
            <span class="input-group-text">Izvajalec in naslov pesmi</span>
        </div>
        <input type="text" name="avtor" class="form-control">
        <input type="text" name="naslov" class="form-control">
    </div>
    <div class="input-group">
        <div class="input-group-prepend">
            <span class="input-group-text">Besedilo</span>
        </div>
        <textarea class="form-control" name="besedilo" rows="5"></textarea>
    </div>
    <button type="submit" class="btn btn-primary">Vnesi podatke</button>
</form>

<hr>

<h3>Besedilna naloga s <em>celoštevilsko rešitvijo</em></h3>
<p>Vnesi navodilo naloge, nato še njeno rešitev in njeno zamišljeno težavnost. Težavnost se bo upoštevala pri številu izkušenj, ki jih dobi igralec, za rešeno nalogo. Nalogo lahko ocenite od 1 (zelo lahka -  samo osnovno računanje), do 5 (precej težka - za rešitev moramo temeljito premisliti in izračunati več stvari).</p>
<form action="/dodaj_nalogo/" method="post">
    <div class="input-group">
        <div class="input-group-prepend">
            <span class="input-group-text">Navodilo</span>
        </div>
        <textarea class="form-control" name="navodilo" rows="5"></textarea>
    </div>
    <div class="input-group">
        <div class="input-group-prepend">
            <span class="input-group-text">Rešitev in težavnost naloge</span>
        </div>
        <input type="text" name="resitev" class="form-control">
        <input type="text" name="tezavnost" class="form-control">
    </div>
    <button type="submit" class="btn btn-primary">Vnesi podatke</button>
</form>










% if error:
    <div class="alert alert-warning alert-dismissible fade show" role="alert">
        <strong>Prišlo je do napake!</strong><br> Morebiti ste nekatera polja pustili prazna ali pa sta dolžina pesmi oziroma težavnost naloge, ki ste ju vpisali, neustrezni.
        <button type="button" class="close" data-dismiss="alert" aria-label="Close">
        <span aria-hidden="true">&times;</span>
        </button>
    </div>
% end

<form action="/" method="get">
    <button type="submit" class="btn btn-danger">Nazaj na začetno stran.</button>
</form>   
