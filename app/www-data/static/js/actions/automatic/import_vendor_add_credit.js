async function import_vendor_add_credit() {
    let modal = document.getElementById("modal-text");
    document.getElementById("action-title").innerText = "Import Vendor";
    let modal_btn = document.getElementById("modal-save-btn")

    value = localStorage.getItem("import_vendor_add_credit");

    if (!value)
        value = 0.5;

    modal.innerHTML = `
    <div class="row">
        <div class="col">
            <div class="input-group mb-3">
                <span class="input-group-text">Vendor</span>
                <select class="form-select form-control-lg" id="vendor-select">
                </select>
            </div>
            <div class="input-group mb-3">
                <span class="input-group-text">Credit</span>
                <input type="number" class="form-control" value="${value}" min="0.5" max="20000" step="0.5"">
                <span class="input-group-text"><i class="bi bi-currency-euro"></i></span>
            </div>
        </div>
    </div>
    `

    const selectElement = document.getElementById("vendor-select");

    let vendors = await (await make_get_request(base_url + `/vendor/`)).json();

    vendors.forEach(vendor => {
        const option = document.createElement("option");
        option.value = vendor.id; // Set the value
        option.textContent = vendor.name; // Set the display text
        selectElement.appendChild(option); // Add the option to the select
    });

    modal_btn.setAttribute("onclick", "import_vendor_add_credit_send(this)")

    const myModalAlternative = new bootstrap.Modal('#action-modal', {});
    myModalAlternative.show();
}

async function import_vendor_add_credit_send(params) {
    let selected_vendor = document.getElementById("modal-text").querySelector("select").value;
    let credit_to_add = document.getElementById("modal-text").querySelector("input").value;

    localStorage.setItem("import_vendor_add_credit", credit_to_add);

    toggleDisable(true);
    await make_post_request(base_url + `/mikai/automations/import_vendor_add_credit`, {
        vendor: selected_vendor,
        credit: credit_to_add
    })
}