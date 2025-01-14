async function importVendor() {
    let modal = document.getElementById("modal-text");
    document.getElementById("action-title").innerText = "Import Vendor";
    let modal_btn = document.getElementById("modal-save-btn")

    modal.innerHTML = `
    <div class="row">
        <div class="col">
            <div class="input-group mb-3">
                <span class="input-group-text">Vendor</span>
                <select class="form-select form-control-lg" id="vendor-select">
                </select>
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

    modal_btn.setAttribute("onclick", "sendImportVendor(this)")

    const myModalAlternative = new bootstrap.Modal('#action-modal', {});
    myModalAlternative.show();
}

async function sendImportVendor(element) {
    let selected_vendor = document.getElementById("modal-text").querySelector("select").value;

    toggleDisable(true);
    await make_post_request(base_url + `/mikai/vendor/import?vendor_id=${selected_vendor}`, {});
}