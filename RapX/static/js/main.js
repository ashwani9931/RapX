// FitnessCh landing page script: BOOK A CLASS button → POST /api/book

document.querySelector(".btn-book")?.addEventListener("click", async () => {
  const msg = document.querySelector(".cta__msg");
  if (!msg) return;
  try {
    const res = await fetch("/api/book", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({}),
    });
    const data = await res.json();
    msg.textContent = data.message ?? "Request received.";
  } catch {
    msg.textContent = "Could not reach the server. Please try again.";
  }
});
