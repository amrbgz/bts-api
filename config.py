# ---------------- SUPABASE CONFIG ----------------
SUPABASE_URL = "https://wdhvzyoqqdcyfwhcuhxl.supabase.co"
SUPABASE_API_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6IndkaHZ6eW9xcWRjeWZ3aGN1aHhsIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzgwNDQ4MDgsImV4cCI6MjA5MzYyMDgwOH0.lg2i1trxvoT6kFfFAl2tquk6ROmvEoSvKmx36pOB8qs"



SUPABASE_HEADERS = {
    "apikey": SUPABASE_API_KEY,
    "Authorization": f"Bearer {SUPABASE_API_KEY}",
    "Content-Type": "application/json"
}
