// Show file name
document.getElementById("imageInput").addEventListener("change", function () {
    let fileName = this.files[0]?.name || "No file selected";
    document.getElementById("fileName").textContent = fileName;
});

// Handle form submit
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

    // Show original image
    document.getElementById("originalPreview").src = URL.createObjectURL(file);

    // Send to backend
    let response = await fetch("/upload", {
        method: "POST",
        body: formData
    });

    let blob = await response.blob();
    let url = URL.createObjectURL(blob);

    // Show enhanced image
    document.getElementById("enhancedPreview").src = url;
});