function renderForm(json, formElement) {
    Object.keys(json).forEach(key => {
        const value = json[key];
        if (typeof value === 'object' && !Array.isArray(value)) {
            // Create a collapsible section for nested objects
            const sectionId = `section-${key}`;
            const section = document.createElement('div');
            section.classList.add('mb-3');

            section.innerHTML = `
          <button class="btn btn-link" type="button" onclick="toggleCollapse('${sectionId}')" aria-expanded="false">
            ${key}
          </button>
          <div class="collapse" id="${sectionId}">
            <div class="card card-body">
            </div>
          </div>
        `;

            formElement.appendChild(section);
            renderForm(value, section.querySelector('.card-body')); // Recursive call
        } else {
            // Render input fields for key-value pairs
            const formGroup = document.createElement('div');
            formGroup.classList.add('mb-3');

            if (typeof value === 'number' || typeof value === 'string') {
                formGroup.innerHTML = `
                <div class="input-group">
                    <span class="input-group-text">${key}</span>
                    <input type="${typeof value === 'number' ? 'number' : 'text'}" class="form-control" name="${key}" value="${value}">
                </div>
                `;
            } else if (typeof value === 'boolean') {
                formGroup.innerHTML = `
                <div class="input-group">
                    <span class="input-group-text">${key}</span>
                    <input type="checkbox" class="btn-check" id="btn-check-5" checked autocomplete="off" onclick="(e) => {console.log(e)}">
                    <label class="btn btn-outline-primary" for="btn-check-5">Checked</label>
                </div>


                `;
            }

            formElement.appendChild(formGroup);
        }
    });
}

async function toggleCollapse(collapseId) {
    var collapseElement = document.getElementById(collapseId);  
    let collapse =  new bootstrap.Collapse(collapseElement);

    collapse.toggle();
}

async function manage_settings() {
    let response = await (await make_get_request(base_url + "/settings/")).json();
    let modal_btn = document.getElementById("modal-save-btn")

    const dynamicForm = document.getElementById("modal-text");
    dynamicForm.innerHTML = "";
    renderForm(response, dynamicForm);

    const sync_buttons = document.createElement("div");
    sync_buttons.classList = ['row'];

    sync_buttons.innerHTML = `
        <div class="col text-end mb-3">
            <button class="btn btn-primary" onclick="sync_db()">Sync</button>
            <button class="btn btn-primary" onclick="full_sync_db()">Full Sync</button>
        </div>
    `;

    dynamicForm.appendChild(sync_buttons);

    modal_btn.setAttribute("onclick", "send_update_settings()")

    const myModalAlternative = new bootstrap.Modal('#action-modal', {});
    myModalAlternative.show();
}

async function sync_db() {
    let url = `${base_url}/sync/sync`;

    let response = await make_get_request(url);

    let data = await response.json();

    if (!response.ok){
        let popup = document.getElementById("error-text");
        popup.innerHTML = data.detail;

        const myModalAlternative = new bootstrap.Modal('#error-modal', {});
        myModalAlternative.show();

        let proggress_bar = document.querySelector("div .progress-bar");
        proggress_bar.style.width = "0%";
        return;
    }
    alert("Sync successfull!");
}

async function full_sync_db() {
    let url = `${base_url}/sync/full_sync`

    let response = await make_get_request(url);

    let data = await response.json();

    if (!response.ok){
        let popup = document.getElementById("error-text");
        popup.innerHTML = data.detail;

        const myModalAlternative = new bootstrap.Modal('#error-modal', {});
        myModalAlternative.show();

        let proggress_bar = document.querySelector("div .progress-bar");
        proggress_bar.style.width = "0%";
        return;
    }
    alert("Sync successfull!");
}

async function send_update_settings() {
    const dynamicForm = document.getElementById("modal-text");
}