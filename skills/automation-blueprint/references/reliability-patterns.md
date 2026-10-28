# Reliability patterns

| Failure mode | Preferred pattern | Common mistake |
|---|---|---|
| Event delivered more than once | Idempotency key + durable deduplication | Assume webhook or scheduler fires exactly once |
| Temporary network/service failure | Timeout + bounded exponential backoff with jitter | Infinite retries or synchronized retry storms |
| Permanent validation/auth error | Fail fast, explain, send to operator | Retry forever |
| Partial multi-step completion | Checkpointed state machine / compensating action | Restart from zero and duplicate completed side effects |
| API throttling | Honor retry-after/quota policy | Ignore rate limits |
| Poison input repeatedly failing | Dead-letter queue or quarantine with reason | Block the entire queue forever |
| Unclear high-impact action | Preview + human approval | Let the model infer consent |
| External publish/write | Draft mode, target check, idempotent request, audit record | Post directly from unverified generated text |
| Secret exposure in logs | Redaction + restricted retention + rotation plan | Store raw request/response logs by default |

## Minimum runbook fields
- Owner and escalation path
- User-visible impact
- Detection signal and threshold
- Safe pause / disable method
- Replay or recovery steps
- Data preservation requirements
- Last successful run and correlation ID
