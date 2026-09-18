export default {
  async fetch(request) {
    const incoming = new URL(request.url);

    const target = new URL(
      incoming.pathname + incoming.search,
      "https://correios-digital.vitorcabral2004.workers.dev"
    );

    return fetch(new Request(target, request));
  },
};
