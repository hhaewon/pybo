const delete_elements = document.querySelectorAll(".delete");
delete_elements.forEach(function (element) {
    element.addEventListener("click", function () {
        if (confirm("정말로 삭제하시겠습니까?")) {
            location.href = this.dataset.uri;
        }
    });
});

const recommend_elements = document.querySelectorAll(".recommend");
recommend_elements.forEach(function (element) {
    element.addEventListener("click", function () {
        if (confirm("정말로 추천하시겠습니까?")) {
            location.href = this.dataset.uri;
        }
    });
});

const contentTextarea = document.querySelector("#content");
let simplemde = new SimpleMDE({
    tabSize: 4,
    element: contentTextarea,
    renderingConfig: {
        singleLineBreaks: false,
        codeSyntaxHighlighting: true,
    },
    toolbar: [
        "bold",
        "italic",
        "heading",
        "|",
        "code",
        "quote",
        "unordered-list",
        "ordered-list",
        "|",
        "link",
        "image",
        "table",
        "|",
        "preview",
        "fullscreen",
    ],
});
hljs.highlightAll();
