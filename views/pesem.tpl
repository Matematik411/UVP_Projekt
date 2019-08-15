% rebase ('base.tpl', title = 'Igra')
% import model

<h1>
    Iskanje manjkajočega dela besedila
</h1>

% if odgovor:
    <h2>Imate nekaj napak</h2>
    <p>
        Odgovorili ste z naslednjimi besedami: {{vnos}} <br>
        Vaša uspešnost: {{uspeh}}
    </p>
% end

<p>Poišči manjkajoče besede in jih v zaporedju vpiši.</p>

<h2>Izvajalec: {{avtor}}. Pesem:{{naslov}}</h2>
<form action="/pesem/" method="post">
    % for i, odsek in enumerate(niz):
        {{odsek}}
        % if i != len(niz) - 1:
            <div class="input-group mb-3 d-inline-flex" style="width: 150px" >
                <select class="custom-select">
                    <option selected >možne besede</option>
                    % for j in premesano[0]:
                        <option name="{{i}}" value="{{j}}">{{premesano[1][j]}}</option>
                    % end
                </select>
            </div>
        % end
    % end
    <button type="submit" class="btn btn-primary">Vnesi rešitev</button>
</form>

