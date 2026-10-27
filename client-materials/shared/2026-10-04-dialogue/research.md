# Source passport

Q2 → https://www.assemblyai.com/docs/billing-and-pricing → fetched → 2026-10-04

> onse. See Understanding input and output tokens for LLM Gateway . LLM Gateway is not covered by the $50 free tier. The free credits granted to new accounts apply to Pre-recorded STT, Real-time STT, Voice Agent API, Speech Understanding, and Guardrails. LLM Gateway usage is billed from your account balance from the first request. In-region endpoints have a 10% surcharge as of July 1, 2026. Requests to the US ( llm-gateway.assemblyai.com ) or EU ( llm-gateway.eu.assemblyai.com ) in-region endpoint

> an still shows Free after subscribing Discounted rates Billing and customer usage tracking How does Auto-pay work? Example Auto-pay and SSO connections Administration Billing and Pricing Copy page Copy page Copy page Copy page AssemblyAI uses pay-as-you-go pricing with no contracts, minimums, or monthly subscriptions. You only pay for what you use, and failed transcripts aren’t charged. For the latest per-hour rates across all models, see the pricing page or the Models pricing section . ​ How bi

>  a successful transcription completes. If a request errors, you aren’t charged for it. Monitor your balance on the Billing page (under Workspace > Settings > Billing in the dashboard ) and enable auto-pay to avoid service interruptions. End-of-month invoicing is available for enterprise customers. Set up billing alerts under Workspace > Settings > Alerts in the dashboard to get notified before your balance runs low. ​ Payment method and invoices AssemblyAI accepts all major credit cards. ACH tra

Q2 → https://www.assemblyai.com/docs/pre-recorded-audio/select-the-speech-model → fetched → 2026-10-04

> ls parameter lets you specify which model(s) to use for transcription. If omitted, it defaults to ["universal-3-5-pro", "universal-2"] . With this default, universal-3-5-pro handles its 18 supported languages; for all other languages, the request will automatically fall back to universal-2 . ​ Available models Python SDK JavaScript SDK API Name Parameter Description Best for Universal-3.5 Pro Recommended speech_models=['universal-3-5-pro'] Our highest accuracy, fastest model with 18-language sup

>  specify which model(s) to use for transcription. If omitted, it defaults to ["universal-3-5-pro", "universal-2"] . With this default, universal-3-5-pro handles its 18 supported languages; for all other languages, the request will automatically fall back to universal-2 . ​ Available models Python SDK JavaScript SDK API Name Parameter Description Best for Universal-3.5 Pro Recommended speech_models=['universal-3-5-pro'] Our highest accuracy, fastest model with 18-language support, native code swi

Q2 → https://www.assemblyai.com/docs/llms-full.txt → fetched → 2026-10-04

> er = Transcriber(api_key="<YOUR_API_KEY>")
> transcript = transcriber.transcribe(audio_file, config)
> 
> for word in transcript.words:
>   print(f"Word: {word.text}, Start: {word.start}, End: {word.end}, Confidence: {word.confidence}")
> ```
> 
> ```python title="Python" highlight={30-31}  expandable
> import requests
> import time
> 
> base_url = "https://api.assemblyai.com"
> 
> headers = {
>     "authorization": "<YOUR_API_KEY>"
> }
> 
> with open("./my-audio.mp3", "rb") as f:
>   response = requests.post(base_url + "/v2/uploa

> nscription-with-gradio-and-python-docs-pre-recorded-audio-guides-gradio-frontend-mdx)
> - [Detect Low Confidence Words in a Transcript](#detect-low-confidence-words-in-a-transcript-docs-pre-recorded-audio-guides-detecting-low-confidence-words-mdx)
> - [Running Bulk Transcription and Load Tests at Scale](#running-bulk-transcription-and-load-tests-at-scale-docs-pre-recorded-audio-guides-bulk-transcription-and-load-tests-at-scale-mdx)
> - [Transcribe Multiple Files Simultaneously Using the JavaScript SDK

Q2 → https://www.assemblyai.com/docs/openapi.yaml → fetched → 2026-10-04

> e transcript and mark it as deleted.
>         <Warning>Files uploaded via the `/upload` endpoint are immediately deleted alongside the transcript when you make a DELETE request, ensuring your data is removed from our systems right away.</Warning>
>       operationId: deleteTranscript
>       x-fern-sdk-group-name: transcripts
>       x-fern-sdk-method-name: delete
>       parameters:
>         - name: transcript_id
>           x-label: Transcript ID
>           in: path
>           description: ID of the transcr

> onses/ServiceUnavailable"
>         "504":
>           $ref: "#/components/responses/GatewayTimeout"
> 
>   /v2/transcript/{transcript_id}:
>     get:
>       tags:
>         - transcript
>       summary: Get transcript
>       operationId: getTranscript
>       x-fern-sdk-group-name: transcripts
>       x-fern-sdk-method-name: get
>       x-fern-request-name: GetTranscriptParams
>       description: |
>         <Note>To retrieve your transcriptions on our EU server, replace `api.assemblyai.com` with `api.eu.assemblyai.com
