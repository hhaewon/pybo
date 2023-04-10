const contentTextarea = document.querySelector("#content");
let simplemde = new SimpleMDE({
    tabSize: 4,
    element: contentTextarea,
    renderingConfig: {
        singleLineBreaks: false,
        codeSyntaxHighlighting: true,
    },
});
// hljs.highlightAll();
