$files = @("index.html","styles.css","app.js","master.html","left-arm.html","vaults.html")
foreach ($f in $files) {
    $url = "https://duke-dynasty.web.app/$f"
    try {
        $res = iwr -UseBasicParsing $url -Method Head
        Write-Output "$f = $($res.StatusCode) ($($res.Headers.'Content-Type'))"
    } catch {
        Write-Output "$f FAILED ($($_.Exception.Message))"
    }
}
