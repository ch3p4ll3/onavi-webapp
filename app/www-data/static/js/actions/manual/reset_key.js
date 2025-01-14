function resetKey() {
    let modal = document.getElementById("modal-text");
    document.getElementById("action-title").innerText = "Export Vendor";
    let modal_btn = document.getElementById("modal-save-btn")

    modal.innerHTML = `
<div class="row">
    <div class="col">
        <h5>Are you sure you want to reset the key?</h5>
    </div>
</div>
`

    modal_btn.setAttribute("onclick", "resetKeySend()")

    const myModalAlternative = new bootstrap.Modal('#action-modal', {});
    myModalAlternative.show();
}

async function resetKeySend() {
    toggleDisable(true);
    await make_post_request(base_url + "/mikai/utils/reset", {})
}