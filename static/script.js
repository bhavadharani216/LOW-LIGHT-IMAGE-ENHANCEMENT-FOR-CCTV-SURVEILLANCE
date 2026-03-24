// ✅ Show selected file name
document.getElementById("imageInput").addEventListener("change", function () {
    let fileName = this.files[0]?.name || "No file selected";
    document.getElementById("fileName").textContent = fileName;
});


// ✅ Handle form submit (UPDATED for multiple outputs)
document.getElementById("uploadForm").addEventListener("submit", async function (e) {
    e.preventDefault();

    let fileInput = document.getElementById("imageInput");
    let file = fileInput.files[0];

    if (!file) {
        alert("Please select an image");
        return;
    }

    let formData = new FormData();
    formData.append("image", file);

    // 🔹 Show original image instantly (preview before processing)
    document.getElementById("originalPreview").src = URL.createObjectURL(file);

    try {
        // 🔹 Send to backend
        let response = await fetch("/upload", {
            method: "POST",
            body: formData
        });

        let data = await response.json();

        // 🔥 Update ALL outputs
        document.getElementById("originalPreview").src = data.original + "?t=" + new Date().getTime();
        document.getElementById("clahePreview").src = data.clahe + "?t=" + new Date().getTime();
        document.getElementById("gammaPreview").src = data.gamma + "?t=" + new Date().getTime();
        document.getElementById("facePreview").src = data.face + "?t=" + new Date().getTime();

    } catch (error) {
        console.error("Error:", error);
        alert("Something went wrong!");
    }
});