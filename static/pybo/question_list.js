const page = document.querySelector("#page");
const hiddenKeywordInput = document.querySelector("#kw");
const searchForm = document.querySelector("#searchForm");
const searchButton = document.querySelector("#btn_search");
const keywordInput = document.querySelector("#search_kw");

const page_elements = document.querySelectorAll(".page-link");
page_elements.forEach(function (element) {
    element.addEventListener("click", function () {
        page.value = this.dataset.page;
        searchForm.submit();
    });
});

function search() {
    hiddenKeywordInput.value = keywordInput.value;
    page.value = 1; // 검색버튼을 클릭할 경우 1페이지부터 조회한다.
    searchForm.submit();
}
btn_search.addEventListener("click", search);

keywordInput.addEventListener("keypress", (element) => {
    if (element.key == "Enter") {
        search();
    }
});
