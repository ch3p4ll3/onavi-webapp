function exportVendor() {
    let modal = document.getElementById("modal-text");
    document.getElementById("action-title").innerText = "Export Vendor";
    let modal_btn = document.getElementById("modal-save-btn")

    modal.innerHTML = `
<div class="row">
    <div class="col">
        <div class="input-group mb-3">
            <span class="input-group-text">Vendor Name</span>
            <input type="text" class="form-control">
        </div>
    </div>
</div>
`

    modal_btn.setAttribute("onclick", "sendExportVendor(this)")

    const myModalAlternative = new bootstrap.Modal('#action-modal', {});
    myModalAlternative.show();
}

async function sendExportVendor(element) {
    let vendor_name = document.getElementById("modal-text").querySelector("input").value;

    toggleDisable(true);
    await make_post_request(base_url + `/mikai/vendor/export?vendor_name=${vendor_name}`, {});
}