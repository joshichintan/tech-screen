import { route } from './router.ts';
import { serve } from './deps.ts';

serve(route, { port: 4001 });
