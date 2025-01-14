base_url = window.location.protocol + '//' + window.location.host;

UUIDs = {
    "addCreditService": {
        "uuid": "619c90d2-045f-4494-838d-c10710f81755",
        "characteristics": [
            {
                "name": "Credit",
                "uuid": "f8c5bdde-3b5b-4726-be63-88d1a6960a5d"
            },
            {
                "name": "Trigger",
                "uuid": "295ad6f5-37f8-495c-972c-c7628bece583"
            }
        ]
    },

    "targetCreditService": {
        "uuid": "38b18113-5a0e-4dc6-a1aa-c1570abd7cbb",
        "characteristics": [
            {
                "name": "Credit",
                "uuid": "71e8ff2c-0142-444e-89a0-1f99b7a7a78d"
            },
            {
                "name": "Trigger",
                "uuid": "a8ea61be-39b1-4906-924b-35e0145c54d5"
            }
        ]
    },

    "setCreditService": {
        "uuid": "8c2eab11-cf01-4924-9e52-f10656303e59",
        "characteristics": [
            {
                "name": "Credit",
                "uuid": "6cf218a4-a71d-4022-8a8b-d8b8282407a6"
            },
            {
                "name": "Trigger",
                "uuid": "0fa372f1-f6dd-4bdb-bb25-b483f3fd3935"
            }
        ]
    },

    "ExportVendorService": {
        "uuid": "ff3f0c79-6979-4038-9dcf-582803a7f741",
        "characteristics": [
            {
                "name": "VendorName",
                "uuid": "69aa82fc-b7fd-4561-a04d-56c75b4079cd"
            },
            {
                "name": "Trigger",
                "uuid": "4d1e27df-1ac9-4f69-bd06-3b13045d0b1d"
            }
        ]
    },

    "ImportVendorService": {
        "uuid": "241ff438-2544-4045-bff9-a4bdb8e713e3",
        "characteristics": [
            {
                "name": "VendorList",
                "uuid": "e57bef5d-9896-4281-ac6a-4095056906eb"
            },
            {
                "name": "SelectedVendor",
                "uuid": "f6ec8d98-3720-4df6-ab7e-d9b7f3b606d7"
            },
            {
                "name": "Trigger",
                "uuid": "b0276bcf-f7ae-4503-bb52-4b9c1a45c0a4"
            }
        ]
    },

    "InfoService": {
        "uuid": "bfc2bc5c-39b5-41fc-be0d-e577272563e6",
        "characteristics": [
            {
                "name": "Version",
                "uuid": "698eb415-817e-41c2-a20b-6b4764d79276"
            },
            {
                "name": "Reset",
                "uuid": "97da1b52-f939-41ee-8c9f-00f83c245acf"
            },
            {
                "name": "Credit",
                "uuid": "11166be1-5422-4ec4-bf06-c1dafbb0f92c"
            },
            {
                "name": "Vendor",
                "uuid": "6511cc88-0439-491a-8a13-63e54dc40410"
            },
            {
                "name": "KeyID",
                "uuid": "b1b96086-aff0-496c-9d75-32dc6f4cb833"
            },
            {
                "name": "Trigger",
                "uuid": "7856bf3c-ee06-4894-9590-288d88bbeef3"
            }
        ]
    },

    "StatusService": {
        "uuid": "7c3eee7a-c3e6-48a6-b7b1-1f81ff46ec9c",
        "characteristics": [
            {
                "name": "Error",
                "uuid": "c43a1d25-426c-4432-970a-0b6482419572"
            },
            {
                "name": "Status",
                "uuid": "f652970c-1d2c-431f-9f9a-16a7094ac0c4"
            }
        ]
    },

    "ResetService": {
        "uuid": "51a5d34b-0547-4519-99a8-512c11c009c2",
        "characteristics": [
            {
                "name": "Trigger",
                "uuid": "8dafcc40-2ce2-4ee3-bb80-71318096be34"
            }
        ]
    }
}