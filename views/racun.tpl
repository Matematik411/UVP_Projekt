% rebase ('base.tpl', title = 'Igra')
% import model

<h1>
    Računska naloga
</h1>

% if odgovor:
    <h2>NAPAKA!</h2>
    <p>
        Odgovorili ste narobe! <br>
        Poskusite ponovno.
    </p>


    % if error: 
        <div class="alert alert-warning alert-dismissible fade show" role="alert">
            Rešitev računa je <strong>celo število</strong>! Ne vpisujte črk ali ostalih neštevilskih znakov.
            <button type="button" class="close" data-dismiss="alert" aria-label="Close">
            <span aria-hidden="true">&times;</span>
            </button>
        </div>
    % end
% end


% operacija = ["+", "-", "*", "//", "%"][znak]
<form action="/racun/" method="post">
    <div class="input-group">
        <div class="input-group-prepend">
            <span class="input-group-text">{{"{0} {1} {2} = ".format(a, operacija, b)}}</span>
        </div>
        <input type="text" name="vnos" class="form-control">
    </div>
    <button type="submit" class="btn btn-primary">Vnesi vrednost</button>
</form>
