import { Status } from "./deps.ts";
import { getSong } from "./repository.ts";

export interface SongRequest {
  id: string;
  req: Request;
}

export function handleRequest(request: SongRequest): Response {
  const req: Request = request.req;
  const relativePath = new URL(req.url).pathname.replace("/api/songs/", "");

  try {
    const song = getSong(relativePath);
    return new Response(JSON.stringify(song), {
      status: 200,
      headers: {
        "content-type": "application/json",
      },
    });
  } catch (err) {
    if (err instanceof Deno.errors.NotFound) {
      return new Response(null, { status: Status.NotFound });
    }
    if (err instanceof Deno.errors.BadResource) {
      return new Response(null, { status: Status.UnprocessableEntity });
    }
  }
  return new Response(null, { status: Status.InternalServerError });
}
