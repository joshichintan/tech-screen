import { Status } from "./deps.ts";
import { handleRequest, SongRequest } from "./controller.ts";
import { appendId } from "./utils.ts";

export async function route(req: Request): Promise<Response> {
  let resp: Response;
  const id = await crypto.randomUUID();
  try {
    if (req.method !== "GET") {
      resp = new Response(null, { status: Status.MethodNotAllowed });
    } else {
      resp = await handleRequest({ id, req } as SongRequest);
    }
  } catch (err) {
    resp = new Response(null, { status: Status.InternalServerError });
  }
  appendId(resp, id);
  return resp;
}
