function targetCredit() {
    let modal = document.getElementById("modal-text");
    document.getElementById("action-title").innerText = "Target Credit";
    let modal_btn = document.getElementById("modal-save-btn");

    value = localStorage.getItem("target_credit");

    if (!value)
        value = 0.5;

    modal.innerHTML = `
    <div class="row">
        <div class="col">
            <div class="input-group mb-3">
                <span class="input-group-text">Credit</span>
                <input type="number" class="form-control" value="${value}" min="0.5" max="20000" step="0.5"">
                <span class="input-group-text"><i class="bi bi-currency-euro"></i></span>
            </div>
        </div>
    </div>
    `

    modal_btn.setAttribute("onclick", "sendTargetCredit(this)")

    const myModalAlternative = new bootstrap.Modal('#action-modal', {});
    myModalAlternative.show();
}

async function sendTargetCredit(element) {
    let credit_to_add = document.getElementById("modal-text").querySelector("input").value;

    localStorage.setItem("target_credit", credit_to_add);

    toggleDisable(true);
    await make_post_request(base_url + `/mikai/credit/target`, {
        "credit": Number(credit_to_add)
    });
}