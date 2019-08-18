% rebase ('base.tpl', title = 'Igra')
% import model

<h1>
    Dopolni besedilo pesmi
</h1>

<div class="alert alert-info" role="alert">
    Spodaj je zapisan del besedila pesmi. Za vsako manjkajočo besedo izberite pravilno in nato vnesite svoje rešitve.
</div>


% if odgovor:
    <div class="alert alert-danger" role="alert">
        <strong>Imate nekaj napak!</strong>
        <br>
        Reševali ste z naslednjo uspešnostjo:
            <hr>
        % for beseda in uspeh:
            {{beseda}}  
        % end
            <hr>
        <p class="mb-0">Poskusite ponovno.</p>
    </div>
% end


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

<hr>
<p>Če je naloga je pretežka, lahko obupate in s tem porabite to nalogo ter izgubite eno točko izkušenj.</p>

<form action="/poraz/" method="post">
    <button type="submit" class="btn btn-danger">Ne znam rešiti naloge.</button>
</form>