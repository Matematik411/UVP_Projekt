% rebase ('base.tpl', title = 'Igra')
% import model

<h1>
    Dodajanje nalog
</h1>

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

% if error:
    <div class="alert alert-warning alert-dismissible fade show" role="alert">
        <strong>Prišlo je do napake!</strong><br> Morebiti ste nekatera polja pustili prazna, ste pri podatkih o pesmih uporabili vejice, ali pa je neustrezna dolžina dela pesmi, ki ste ga vpisali.
        <button type="button" class="close" data-dismiss="alert" aria-label="Close">
        <span aria-hidden="true">&times;</span>
        </button>
    </div>

