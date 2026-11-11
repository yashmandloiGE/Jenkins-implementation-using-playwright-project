
from playwright.sync_api import expect


# Test Case 1: File Upload
def test_file_upload(page, tmp_path):

    # Create a sample file
    upload_file = tmp_path / "sample.txt"
    upload_file.write_text("QA Automation Practice")

    # Create webpage with file input
    page.set_content("""
        <input type="file" id="file-upload">

        <p id="result"></p>

        <script>
            document.querySelector("#file-upload")
                .addEventListener("change", function() {
                    document.querySelector("#result").innerText =
                        this.files[0].name;
                });
        </script>
    """)

    # Upload file
    page.locator("#file-upload").set_input_files(str(upload_file))

    # Verify uploaded file
    expect(page.locator("#result")).to_have_text("sample.txt")


# Test Case 2: File Download
def test_file_download(page, tmp_path):

    # Create a webpage and simulate a downloadable file
    def handle_route(route):

        if "/download/report.txt" in route.request.url:

            route.fulfill(
                status=200,
                body="QA Automation Download Report",
                headers={
                    "Content-Disposition": 'attachment; filename="report.txt"',
                    "Content-Type": "text/plain"
                }
            )

        else:

            route.fulfill(
                status=200,
                content_type="text/html",
                body="""
                    <a href="/download/report.txt">
                        Download report
                    </a>
                """
            )

    page.route("**/*", handle_route)

    page.goto("http://qa.test/")

    # Capture download
    with page.expect_download() as download_info:

        page.get_by_role(
            "link",
            name="Download report"
        ).click()

    download = download_info.value

    # Save downloaded file
    download_path = tmp_path / download.suggested_filename

    download.save_as(str(download_path))

    # Verify download
    assert download.suggested_filename == "report.txt"

    assert download_path.read_text() == "QA Automation Download Report"

    print("File uploaded and downloaded successfully!")
