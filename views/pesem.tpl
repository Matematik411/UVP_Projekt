% rebase ('base.tpl', title = 'Igra')
% import model

<h1>
    Dopolni besedilo pesmi
</h1>

% if odgovor:
    <div class="alert alert-danger" role="alert">
        <strong>Imate nekaj napak!</strong>
        <br>
        <p>Reševali ste z naslednjo uspešnostjo:
            <hr>
        % for beseda in uspeh:
            {{beseda}}  
        % end
            <hr>
        Poskusite ponovno.
        </p>
    </div>
% end

<p>Izberi manjkajočo besedo in s tem dopolni besedilo pesmi</p>
<hr>

<h3>Izvajalec: <strong>{{avtor}}</strong><br>
    Pesem: <em>{{naslov}}</em>
</h3>
<form action="/pesem/" method="post">
    % for i, odsek in enumerate(odseki):
        {{odsek}}
        % if i != len(odseki) - 1:
            <div class="input-group d-inline-flex" style="width: 150px" >
                <select class="custom-select" name="{{i}}">
                    <option selected >možne besede</option>
                    % for j in premesano[0]:
                        <option value="{{j}}">{{premesano[1][j]}}</option>
                    % end
                </select>
            </div>
        % end
    % end
    <button type="submit" class="btn btn-primary align-self-end">Vnesi rešitev</button>
</form>

