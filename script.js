document.addEventListener("DOMContentLoaded", function () {
    const netherToSurfaceRadio = document.getElementById("netherToSurface");
    const surfaceToNetherRadio = document.getElementById("surfaceToNether");
    const xInput = document.getElementById("xInput");
    const zInput = document.getElementById("zInput");
    const convertButton = document.getElementById("convertButton");
    const result = document.getElementById("result");

    convertButton.addEventListener("click", function () {
        const x = parseFloat(xInput.value);
        const z = parseFloat(zInput.value);
        let convertedX, convertedZ;

        if (netherToSurfaceRadio.checked) {
            convertedX = x / 8;
            convertedZ = z / 8;
        } else {
            convertedX = x * 8;
            convertedZ = z * 8;
        }

        result.textContent = `Coordenadas Convertidas: X = ${convertedX.toFixed(2)}, Z = ${convertedZ.toFixed(2)}`;
    });
});
