% rebase ('base.tpl', title = 'Igra')
% import model

<h1>
    Besedilna naloga
</h1>

% if odgovor:
    <div class="alert alert-danger" role="alert">
        <strong>Napačen odgovor!</strong>
        <hr>
        <p>Odgovorili ste narobe. Poskusite ponovno.</p>
    </div>



    % if error: 
        <div class="alert alert-warning alert-dismissible fade show" role="alert">
            Rešitev računa je <strong>celo število</strong>! Ne vpisujte črk ali ostalih neštevilskih znakov.
            <button type="button" class="close" data-dismiss="alert" aria-label="Close">
            <span aria-hidden="true">&times;</span>
            </button>
        </div>
    % end
% end

<h3>Navodila naloge</h3>
<p>{{navodilo}}</p>

<form action="/besedilna/" method="post">
    <div class="input-group mb-3">
        <input type="text" class="form-control" name="vnos">
    </div>
    <button type="submit" class="btn btn-primary">Vnesi vrednost</button>
</form>

<hr>
<p>Če je naloga je pretežka, lahko obupate in s tem porabite to nalogo ter izgubite eno točko izkušenj.</p>

<form action="/poraz/" method="post">
    <button type="submit" class="btn btn-danger">Ne znam rešiti naloge.</button>
</form>
