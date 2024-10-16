$(document).ready(function() {
    $("#main-form").on("submit", async function(e) {
        e.preventDefault();
      
        const jQSubmitter = $(e.originalEvent.submitter);
        if (jQSubmitter.attr("data-class") === "btn--no-submit") {
            switch (jQSubmitter.attr("id")) {
                case "btn--cancel-image-uploads":
                    $("#images-input").val("");
                    break;
                case "btn--cancel-delete-images":
                    $("#delete_images-input").val("");
                    break;
            }
            return;
        }

        let formData = new FormData(e.target, e.originalEvent.submitter);
        const respJson = await fetchWrapper(window.location.href, {method: "POST", body: formData});
        doAjaxResponseForm(respJson, e);
    });
});
