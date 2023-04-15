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
// hljs.highlightAll();
