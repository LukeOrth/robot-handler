 document.addEventListener("DOMContentLoaded", () => {
    // Code to handle searching the whole table
    tsInputField = document.querySelector("#search-table")
    
    tsInputField.addEventListener("input", () => {
        const tsQuery = tsInputField.value.toLowerCase();
        const table = document.querySelector(".searchable-table");
        const tsTableRows = table.querySelectorAll("tbody > tr");

        for (const tableCell of tsTableRows) {
            const row = tableCell.closest("tr");
            const value = tableCell.textContent.toLowerCase().replace(",", "");

            row.style.visibility = null;
            
            if (value.search(tsQuery) !== -1) {
                let rows = table.querySelectorAll(`.${row.className}`);
                for (r of rows) {
                    r.style.visibility = "visible";
                }
            } else {
                row.style.visibility = "collapse";
            }
        }
    });
    
    // Code to handle searching by columns
    document.querySelectorAll(".search-column").forEach((csInputField) => {
        const csTableRows = csInputField
            .closest("table")
            .querySelectorAll("tbody > tr");
        const headerCell = csInputField.closest("th");
        const otherHeaderCells = headerCell.closest("tr").children;
        const columnIndex = Array.from(otherHeaderCells).indexOf(headerCell);
        const searchableCells = Array.from(csTableRows).map(
            (row) => row.querySelectorAll("td")[columnIndex]
        );

        csInputField.addEventListener("input", () => {
            const csQuery = csInputField.value.toLowerCase();
            for (const tableCell of searchableCells) {
                if (tableCell) {
                    const row = tableCell.closest("tr");
                    const value = tableCell.textContent.toLowerCase().replace(",", "");

                    row.style.visibility = null;

                    if (value.search(csQuery) === -1) {
                        row.style.visibility = "collapse";
                    }
                }
            }
        });
    });
});
