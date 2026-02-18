# ---- Builder stage: install only runtime deps into a user site-packages dir ----
FROM python:3.11-slim AS builder

WORKDIR /build

# Copy only requirements first to maximize Docker layer caching
COPY app/requirements.txt .

# Install runtime dependencies (pinned) into /root/.local
RUN pip install --user --no-cache-dir -r requirements.txt


# ---- Runtime stage: minimal image with only what we need to run ----
FROM python:3.11-slim

WORKDIR /app

# Copy installed deps from builder (no compiler/toolchain carried over)
COPY --from=builder /root/.local /root/.local

# Copy application code
COPY app/ .

# Make the user-installed binaries available (uvicorn)
ENV PATH=/root/.local/bin:$PATH

EXPOSE 8000

# Run the API
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
